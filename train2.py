"""This module implements data feeding and training loop to create model
to classify X-Ray chest images as a lab example for BSU students.
"""

__author__ = 'Alexander Soroka, soroka.a.m@gmail.com'
__copyright__ = """Copyright 2020 Alexander Soroka"""


import argparse
import glob
import numpy as np
import tensorflow as tf
import time
from tensorflow.python import keras as keras
from tensorflow.python.keras.callbacks import LearningRateScheduler
from keras.models import load_model


LOG_DIR = 'logs'
SHUFFLE_BUFFER = 10
BATCH_SIZE = 8
NUM_CLASSES = 2
PARALLEL_CALLS=4
RESIZE_TO = 224
TRAINSET_SIZE = 5216
VALSET_SIZE=624


def parse_proto_example(proto):
    keys_to_features = {
        'image/encoded': tf.FixedLenFeature((), tf.string, default_value=''),
        'image/class/label': tf.FixedLenFeature([], tf.int64, default_value=tf.zeros([], dtype=tf.int64))
    }
    example = tf.parse_single_example(proto, keys_to_features)
    example['image'] = tf.image.decode_jpeg(example['image/encoded'], channels=3)
    example['image'] = tf.image.convert_image_dtype(example['image'], dtype=tf.float32)
    example['image'] = tf.image.resize_images(example['image'], tf.constant([RESIZE_TO, RESIZE_TO]))
    return example['image'], example['image/class/label']


def normalize(image, label):
    return tf.image.per_image_standardization(image), label

def resize(image, label):
    return tf.image.resize_images(image, tf.constant([RESIZE_TO, RESIZE_TO])), label

def create_dataset(filenames, batch_size):
    """Create dataset from tfrecords file
    :tfrecords_files: Mask to collect tfrecords file of dataset
    :returns: tf.data.Dataset
    """
    return tf.data.TFRecordDataset(filenames)\
        .map(parse_proto_example)\
        .map(resize)\
        .map(normalize)\
        .shuffle(buffer_size=5 * batch_size)\
        .repeat()\
        .batch(batch_size)\
        .prefetch(2 * batch_size)


class Validation(tf.keras.callbacks.Callback):
    def __init__(self, log_dir, validation_files, batch_size):
        self.log_dir = log_dir
        self.validation_files = validation_files
        self.batch_size = batch_size

    def on_epoch_end(self, epoch, logs=None):
        print('The average loss for epoch {} is {:7.2f} '.format(
            epoch, logs['loss']
        ))

        validation_dataset = create_dataset(self.validation_files, self.batch_size)
        validation_images, validation_labels = validation_dataset.make_one_shot_iterator().get_next()
        validation_labels = tf.one_hot(validation_labels, NUM_CLASSES)

        result = self.model.evaluate(
            validation_images,
            validation_labels,
            steps=int(np.ceil(VALSET_SIZE / float(BATCH_SIZE)))
        )
        callback = tf.keras.callbacks.TensorBoard(log_dir=self.log_dir, update_freq='epoch', batch_size=self.batch_size)

        callback.set_model(self.model)
        callback.on_epoch_end(epoch, {
            'val_' + self.model.metrics_names[i]: v for i, v in enumerate(result)
        })


def build_model():
    model = keras.models.load_model('model.h5')
    model.trainable = True
    #base_model = tf.keras.applications.VGG16(include_top=False, weights='imagenet', input_shape=(224,224,3), classes=2)
    #base_model.trainable = False
    return model
    #tf.keras.models.Sequential([
    #	base_model,
    #	tf.keras.layers.Flatten(),
    #    tf.keras.layers.Dense(NUM_CLASSES, activation=tf.keras.activations.softmax)
    #])



def main():
    args = argparse.ArgumentParser()
    args.add_argument('--train', type=str, help='Glob pattern to collect train tfrecord files')
    args.add_argument('--test', type=str, help='Glob pattern to collect test tfrecord files')
    args = args.parse_args()

    train_dataset = create_dataset(glob.glob(args.train), BATCH_SIZE)
    train_images, train_labels = train_dataset.make_one_shot_iterator().get_next()
    train_labels = tf.one_hot(train_labels, NUM_CLASSES)

    model = build_model()

    model.compile(
        optimizer=keras.optimizers.sgd(lr=0.00000000001, momentum=0.9),
        loss=tf.keras.losses.categorical_crossentropy,
        metrics=[tf.keras.metrics.categorical_accuracy],
        target_tensors=[train_labels]
    )

    log_dir='{}/xray-{}'.format(LOG_DIR, time.time())
    model.fit(
        (train_images, train_labels),
        epochs=150,
        steps_per_epoch=int(np.ceil(TRAINSET_SIZE / float(BATCH_SIZE))),
        callbacks=[
            tf.keras.callbacks.TensorBoard(log_dir),
            Validation(log_dir, validation_files=glob.glob(args.test), batch_size=BATCH_SIZE)
        ]
    )
    #model.save('model.h5')


if __name__ == '__main__':
    main()

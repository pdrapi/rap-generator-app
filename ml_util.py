import tensorflow as tf
import logging
import numpy as np
import os
import time
import json
import pandas

class MLUtil():
    #Class with ML functions to generate lyrics with the use of pre-trained model
    
    char2idx = None
    idx2char = None

    def __init__(self):
        self.prep_ml()
        
    def prep_ml(self):
        #opening needed files/dicts for the ML model to work
        
        logging.info("Initializing ML prep")

        with open('char2idx.json', 'r') as f:
            MLUtil.char2idx = json.load(f)

        idx2char = []
        with open("idx2char.txt") as f:
            for line in f:
                idx2char.append(line)

        idx2char = list(map(lambda x: x.strip("\n"), idx2char))
        idx2char.insert(0, "\n")
        idx2char.remove("")
        idx2char.remove("")
        MLUtil.idx2char = idx2char

        logging.info("ML prep completed")

    def generate_text(self, num_generate, temperature, start_string):
        # predicts next letters based on above variables & predefined model
        num = int(num_generate)
        temp = float(temperature)
        word = start_string
        char2idx = MLUtil.char2idx
        idx2char = MLUtil.idx2char

        model = tf.keras.models.load_model(
            'good_model_100_epochs.h5', compile=False)

        # Converting our start string to numbers (vectorizing)
        input_eval = [char2idx[s] for s in word]
        input_eval = tf.expand_dims(input_eval, 0)

        # Empty string to store our results
        text_generated = []

        # Here batch size == 1
        model.reset_states()
        for i in range(num):
            predictions = model(input_eval)

            # remove the batch dimension
            predictions = tf.squeeze(predictions, 0)

            # using a categorical distribution to predict the character returned by the model
            predictions = predictions / temp
            predicted_id = tf.random.categorical(
                predictions, num_samples=1)[-1, 0].numpy()

            # We pass the predicted character as the next input to the model
            # along with the previous hidden state
            input_eval = tf.expand_dims([predicted_id], 0)

            text_generated.append(idx2char[predicted_id])

        result = start_string + ''.join(text_generated)

        return result

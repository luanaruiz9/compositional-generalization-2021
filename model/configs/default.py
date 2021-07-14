# Copyright 2021 The Flax Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Default Hyperparameter configuration."""

import ml_collections


def get_config():
  """Get the default hyperparameter configuration."""
  config = ml_collections.ConfigDict()

  # Path to load or store sentencepiece vocab file.
  config.vocab_path = None

  # Vocabulary size if `vocab_path` is not given.
  config.vocab_size = 535
  config.max_corpus_chars = 10**7

  # Name of TFDS PCFG dataset to use.
  config.dataset_name = "pcfg_full_data"
  config.train_split = "it_dec_train"

  # Optional name of TFDS PCFG dataset to use for evaluation.
  config.eval_dataset_name = None
  config.eval_split = "it_dec_val"
  config.predict_split = "it_dec_test"

  # Per device batch size for training.
  config.per_device_batch_size = 64

  # Beam size for inference.
  config.beam_size = 4

  config.num_train_steps = 10_000

  # Number of steps to take during evaluation.
  config.num_eval_steps = 1
  # Number of steps to generate predictions.
  # -1 will use the whole eval dataset.
  config.num_predict_steps = -1
  # Number of steps to take during evaluation of training set.
  config.num_eval_train_steps = 5
  # Number of steps to generate predictions on the training set.
  # -1 will use the whole training dataset.
  config.num_predict_steps_train = 5

  # Max prediction loops for prediction dataset.
  config.num_predict_loops = 20
  # Whether to use annotated number of operations to limit number of loops.
  config.use_annotations = True
  # Extra loops in addition to annotations.
  config.extra_loops = 2

  # Base learning rate.
  config.learning_rate = 0.0625

  # Linear learning rate warmup.
  config.warmup_steps = 4000

  # Cross entropy loss label smoothing.
  config.label_smoothing = 0.1

  # Decay factor for AdamW style weight decay.
  config.weight_decay = 0.0

  # Maximum length cutoff for training examples.
  config.max_target_length = 256
  # Maximum length cutoff for eval examples.
  config.max_eval_target_length = 256
  # Maximum length cutoff for predicted tokens.
  config.max_predict_length = 256
  # Inputs and targets share embedding.
  config.share_embeddings = True

  # Final logit transform uses embedding matrix transpose.
  config.logits_via_embedding = True

  # Number of transformer layers.
  config.num_layers = 6

  # Size of query/key/value for attention.
  config.qkv_dim = 64
  # Size of embeddings.
  config.emb_dim = 64
  # Size of the MLP.
  config.mlp_dim = 256

  # Number of attention heads.
  config.num_heads = 4

  # Dropout rate.
  config.dropout_rate = 0.1

  # Attention dropout rate.
  config.attention_dropout_rate = 0.1

  # Whether to save model checkpoints.
  config.save_checkpoints = True
  # Whether to restore from existing model checkpoints.
  config.restore_checkpoints = True
  # Just do prediction from saved checkpoint.
  config.just_do_pred = True

  # Save a checkpoint every these number of steps.
  config.checkpoint_every_steps = 5_000
  # Frequency of eval during training, e.g. every 1000 steps.
  config.eval_every_steps = 1_250

  # Use bfloat16 mixed precision training instead of float32.
  config.use_bfloat16 = True

  # Integer for PRNG random seed.
  config.seed = 0

  return config

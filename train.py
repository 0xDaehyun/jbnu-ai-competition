from transformers import Trainer, TrainingArguments
from config import *

def train_model(model, tokenizer, train_dataset, val_dataset):
    training_args = TrainingArguments(
        output_dir="./results",
        per_device_train_batch_size=BATCH_SIZE,
        per_device_eval_batch_size=BATCH_SIZE,
        num_train_epochs=NUM_EPOCHS,
        learning_rate=LEARNING_RATE,
        weight_decay=0.01,
        logging_dir="./logs",
        logging_steps=50,
        save_total_limit=1,
        do_train=True,
        do_eval=True,
        report_to="none"
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        tokenizer=tokenizer
    )

    trainer.train()
    return trainer
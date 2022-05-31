python context2vec/train/corpus_by_sent_length.py data_processed/product_comment_processed.txt 128
python context2vec/train/train_context2vec.py -i data_processed/product_comment_processed.txt.DIR  -w  WORD_EMBEDDINGS -m MODEL  -c ls
tm --deep yes -t 3 --dropout 0.0 -u 300 -e 10 -p 0.75 -b 100
import random
import copy
def weighted_draw_from_dict(prob_dict):
    # Utility function -- do not modify
    # Randomly choose a key from a dict, where the values are the relative probability weights.
    # http://stackoverflow.com/a/3679747/86684
    choice_items = prob_dict.items()
    total = sum(w for c, w in choice_items)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choice_items:
       if upto + w > r:
          return c
       upto += w
    assert False, "Shouldn't get here"


## ---------------------- write your answers below here -------------------


def draw_next_word_unigram_model(uni_counts):
    return weighted_draw_from_dict(uni_counts)

def draw_next_word_bigram_model(uni_counts, bi_counts, prev_word):
    denominator = 0
    if prev_word in uni_counts:
       denominator = uni_counts[prev_word]
    else:
        print ("That word never occured before ! Cannot account for it without laplace smoothing") 
    temp_storage={}
    temp_storage= copy.deepcopy(bi_counts)
    if prev_word in temp_storage:
        temp_storage[prev_word].update((x, y/denominator) for x, y in temp_storage[prev_word].items())
        next_word=weighted_draw_from_dict(temp_storage[prev_word])
        #bi_counts[prev_word][next_word]+=1  # Optional code for re-training the dataset and updating the probabilities
        #uni_counts[prev_word]+=1            # and counts of words as they are predicted to make future predictions better.
    else:
         print (" No relevant data ! Cannot account for it without laplace smoothing")
    return next_word


def sample_sentence(uni_counts, bi_counts):
    tokens = ['**START**']
    index=0
    next_word= ""
    while next_word != '**END**':
        next_word= draw_next_word_bigram_model(uni_counts,bi_counts,tokens[index])
        tokens.append(next_word)
        index+=1
    return tokens


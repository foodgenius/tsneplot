# tsneplot - t-SNE for Humans

CLI tool/library for quick & dirty visualizations of word2vec models. Uses the
t-SNE (t-Distributed Stochastic Neighbor Embedding) method provided in
scikit-learn.

Inspiration for some of the code comes from this [blog post](https://medium.com/@aneesha/using-tsne-to-plot-a-subset-of-similar-words-from-word2vec-bb8eeaea6229).

## Install
```
cd tsneplot

python setup.py install --user
```

## Usage

As CLI
```
# Display a scatterplot of all words in the vocab (takes a while, depending).
tsneplot display_all --model <path_to_model>

# Display the neighborhood of a particular word or words
tsneplot display_words --model <path_to_model> chicken salad parmesan
```

As a library
```
import tsneplot

model = tsneplot.load_model('<path_to_model>')

tsneplot.display_all(model)
tsneplot.display_words(model, ['chicken', 'salad', 'parmesan'])
```

## Screenshots
![Display All](https://github.com/foodgenius/tsneplot/raw/master/display_all.png)
![Chicken and beef](https://github.com/foodgenius/tsneplot/raw/master/display_words.png)


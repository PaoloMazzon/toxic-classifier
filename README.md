# Toxic Classifier

This is a tool to classify the percieved toxicity of a given string of text.
It is to demonstrate the effectiveness of the toxicity regression model in
`model/` by providing the user with a small REPL that they can play with.

## Effectiveness

The model is a linear regression model trained on the Jigsaw Unintended Bias 
dataset with a 7% error rate on the test data. It is hypothetically very 
effective at rating the toxicity of input strings, but it is not particularly
great at estimating whether or not a string ***is*** toxic. That is to say,
this model is not suitable to check if a given string is toxic, but rather it
is a good way to confirm that something is toxic if you already have suspicion
that a given string is toxic (for example, if player A reports player B for 
for toxicity and the input string is some chat from player B).
# IaC Collection

This is an incomplete and very much in-progress collection for all kinds of IaC blueprints I have accumulated over the years. 
I realized there's tons of infra code I have stored across many different repos and I kept searching for it again and again. Because this is a waste of time, I will gradually move the usable & relevant stuff in here. 
I made this public because I believe in open source, even if it means just sharing my own random stuff. Feel free to copy & paste as needed.

## Standard of quality
While I used all the code in here successfully, this isn't a collection of "gold standards" or ", merely things I have found to be useful. 
All of the code in here has been used by me and so I consider it to be tested and functional. 
However, almost all of the Terraform and quite a bit of the non-TF-stuff will require additional configuration (which I usually store in a secret.tf.vars or similar), because I don't want to publicly commit my actual configuration details for obvious reasons.

## Warning
Make sure you understand what you are doing before you apply any of this! When it comes to Terraform (and IaC in general), you can do a lot of damage, and more importantly incur a lot of costs if you spin up random resources. I made sure to spec conservatively wherever applicable but use your own brain.


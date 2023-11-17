# Progress Report 
## Team Member
Shan Huang - sh69@illinois.edu
## Progress made so far
1. Found the model could be easily used for code summarization tasks. [(github repo)](https://github.com/agemagician/CodeTrans/blob/main/prediction/single%20task/source%20code%20summarization/python/t5%20interface/base_model.ipynb)
2. Finish the Chrome Extension for code summarization

## Remaining tasks
1. Decoration for UI and ICON
2. Finetune model(if more time)
3. Write the environment setup scripts for easy installation
4. Find Dataset and test for the extension to see what code summarization could be made (the model accuracy is 15% for Python)
5. Document and present the results.
## Any challenges/issues being faced.
1. Found the model could be easily used for code summarization tasks.
    - Browsed multiple Github repos and papers online and found most models are outdated or need to be trained. [CodeTrans](https://github.com/agemagician/CodeTrans/tree/main) is a model not require training and provided Python package could be installed by pip
    - Browsing the entire repo to find the correct script to run the code summarization task
2. Develop the Chrome Extension
    - Understand the basics for developing Chrome Extension
        - Look at the [manual](https://developer.chrome.com/docs/extensions/)
    - How to embed the Python code into the Chrome extension
        - Tried to use PyScript -> However, PyScript does not support large libraries like torch (x)
        - Now tried to data exchange by Flask
    - Flask does not get responses or send responses
        - Look at the post [here](https://stackoverflow.com/questions/69992584/body-of-js-request-not-appearing-in-flask)
        - Implement CORS for Flask to allow access from all domains

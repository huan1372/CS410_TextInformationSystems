from flask import Flask,request,jsonify
from flask_cors import CORS
from transformers import AutoTokenizer, AutoModelWithLMHead, SummarizationPipeline
import tokenize
import io
import json

app = Flask(__name__)
CORS(app)

pipeline = SummarizationPipeline(
	model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_base_source_code_summarization_python"),
	tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_base_source_code_summarization_python", skip_special_tokens=True),
	device="mps")

@app.route('/', methods=['POST'])
def segment_code():
    data =  json.loads(request.get_data())
    line = data['code_segment']
    print(line)
    result= []
    line = io.StringIO(line) 
    for toktype, tok, start, end, line in tokenize.generate_tokens(line.readline):
        if (not toktype == tokenize.COMMENT):
            if toktype == tokenize.STRING:
                result.append("CODE_STRING")
            elif toktype == tokenize.NUMBER:
                result.append("CODE_INTEGER")
            elif (not tok=="\n") and (not tok=="    "):
                result.append(str(tok))

    tokenized_code = ' '.join(result)
    summary = pipeline([tokenized_code])
    output = {'result': summary[0]["summary_text"]}
    print(output)
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)

# ProcessLLM

This GitHub-Repository describes the development of the  ProcessLLM - a large language model specialized on the interpretation, analysis, and optimization of processes in BPMN-Notation. The purpose of this GitHub-repository is to augment the corresponding paper "ProcessLLM: A large language model specialized on the interpretation, analysis, and optimization of business processes" with additional technical insights into the development of the artefact.

## Structure of the repository
This repository consists of the three folders "Documentation", "text-generation-webui", and "Chatbot-interface".
- **Documentation**: This folder provides a detailed documentation of the different steps conducted to achieve the final ProcessLLM. This includes the setup of the environment, the development of the ProcessLLM, incorporating data preparation, base model selection, unsupervised fine-tuning, supervised fine-tuning, and instantiation, and the evaluation of the ProcessLLM from a quantitative and qualitative point of view.
- **text-generation-webui**: This folder provides the text-generation-webui developed by Oobabooga (https://github.com/oobabooga/text-generation-webui) in which the development of the ProcessLLM as well as the quantitative evaluation of the ProcessLLM took place. Furthermore, the datasets used for the training and the evaluation of the ProcessLLM are already included into the text-generation-webui in the folder "text-generation-webui/training". The webui including the datasets can be used the reproduce the ProcessLLM. The detailed description of the training process is provided in the "Documentation"-folder.
- **Chatbot-interface**: This folder provides the gradio-app that was used to instantiate the ProcessLLM and to conduct the qualitative evaluation of it. A detailed description on how the evaluation process was conducted is described in the "Documentation"-folder.
- **Supplementary-materials**: This folder provides supplementary materials as e.g. the questionaire used in EVAL1 and EVAL2.

## Testing the ProcessLLM
The descriptions provided in the "Documentation"-folder can be used to reproduce the ProcessLLM over the text-generation-webui and to evaluate it over the gradio-app in the Chatbot-interface-folder. However, you can also directly use the final ProcessLLM. This model is provided over huggingface: https://huggingface.co/ProcessLLM-developers/ProcessLLM. Furthermore, this huggingface-llm is also already deposited in the file "Gradio_app.py" and will therefore be used as the default.


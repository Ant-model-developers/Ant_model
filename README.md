# Ant-model

This GitHub-Repository describes the development of the Ant-model - a large language model specialized on the interpretation, analysis, and optimization of processes in BPMN-Notation. The purpose of this GitHub-repository is to augment the corresponding paper "Ant-model: A large language model specialized on the interpretation, analysis, and optimization of BPMN processes" with additional technical insights into the development of the artefact.

## Structure of the repository
This repository consists of the three folders "Documentation", "text-generation-webui", and "Humanisitic_evaluation".
- **Documentation**: This folder provides a detailed documentation of the different steps conducted to achieve the final ant-model. This includes the setup of the environment, the development of the ant-model, incorporating data preparation, base model selection, unsupervised fine-tuning and supervised fine-tuning, and the evaluation of the ant-model from a numeric and humanistic point of view.
- **text-generation-webui**: This folder provides the text-generation-webui developed by Oobabooga (https://github.com/oobabooga/text-generation-webui) in which the development of the ant-model as well as the numeric evaluation of the ant-model took place. Furthermore, the datasets used for the training and the evaluation of the ant-model are already included into the text-generation-webui in the folder "text-generation-webui/training". The webui including the datasets can be used the reproduce the ant-model. The detailed description of the training process is provided in the "Documentation"-folder.
- **Humanistic_evaluation**: This folder provides the gradio-app that was used to conduct the humanistic-evaluation of the ant-model. A detailed description on how the evaluation process was conducted is described in the "Documentation"-folder.

## Testing the Ant-model
The descriptions provided in the "Documentation"-folder can be used to reproduce the Ant-model over the text-generation-webui and to evaluate it over the gradio-app in the humanistic_evaluation-folder. However, you can also directly use the final ant-model. This model is provided over huggingface: https://huggingface.co/Ant-model-developers/Ant_model. Furthermore, this huggingface-llm is also already deposited in the file "Humanistic_evaluation.py" and will therefore be used as the default.


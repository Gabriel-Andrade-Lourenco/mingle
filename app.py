# import streamlit as st
# import requests
# import base64

# API_KEY = "g57u89pklmnuygfdraswxcd"
# HEADERS = {
#     "x-api-key": API_KEY
# }

# PAGE_SELECTION_KEY = "page_selection"
# ENDPOINT_URL = "https://7ryvoj1rfa.execute-api.us-east-1.amazonaws.com/prod"

# selected_archives = []

# if PAGE_SELECTION_KEY not in st.session_state:
#     st.session_state[PAGE_SELECTION_KEY] = "Adicione Empresa"

# # create_company_page = st.sidebar.button("Adicione Empresa")
# # update_company_page = st.sidebar.button("Atualize Empresa")
# # company_page = st.sidebar.button("Empresas")
# # chat_page = st.sidebar.button("Chat")

# # if create_company_page:
# #     st.session_state[PAGE_SELECTION_KEY] = "Adicione Empresa"
# # elif company_page:
# #     st.session_state[PAGE_SELECTION_KEY] = "Empresas"
# # elif chat_page:
#     st.session_state[PAGE_SELECTION_KEY] = "Chat"
# # elif update_company_page:
# #     st.session_state[PAGE_SELECTION_KEY] = "Atualize Empresa"

# # if st.session_state[PAGE_SELECTION_KEY] == "Adicione Empresa":
# #     st.title("🏢 Adicione Empresa")
# #     id = st.text_input("Empresa ID")
# #     company_name = st.text_input("Nome da Empresa")
# #     prompt = st.text_input("Prompt")

# #     st.write("Selecione uma opção:")
# #     option = st.radio("Escolha entre passar um documento ou uma lista de URLs", ("Documento", "Links"))

# #     if option == "Documento":
# #         document_type = st.selectbox("Tipo de Documento", ["csv", "pdf", "txt", "doc", "docx"])

# #         document_file = st.file_uploader("Upload", type=["csv", "pdf", "txt", "doc", "docx"])

# #         create_company_button = st.button("Adicionar Empresa", key="create_company")

# #         if create_company_button and document_file:
# #             base64_content = base64.b64encode(document_file.getvalue()).decode()

# #             api_data = {
# #                 "company_id": id,
# #                 "company_name": company_name, 
# #                 "prompt": prompt,
# #                 "documentType": document_type,
# #                 "documentContent": base64_content,
# #                 "documentName": document_file.name.split('.')[0]
# #             }

# #             try:
# #                 response = requests.post(ENDPOINT_URL + "/company", json=api_data, headers=HEADERS)
# #                 if response.status_code == 200:
# #                     st.success(f"Empresa '{company_name}' criada com sucesso!")
# #                 else:
# #                     st.error("Falha ao criar a empresa. Por favor, tente novamente.")
# #             except Exception as e:
# #                 st.error(f"Um erro ocorreu: {str(e)}")

    
# #     elif option == "Links":
# #         st.subheader("Lista de URLs")
# #         urls = st.text_input("Novo item")

# #         if "lista" not in st.session_state:
# #             st.session_state["lista"] = []

# #         if st.button('Adicionar'):
# #             if urls:
# #                 st.session_state.lista.append(urls)

# #         if st.session_state.lista:
# #             lista_str = "\n".join(st.session_state.lista)
# #             st.text_area("Itens da Lista", value=lista_str, height=200)

# #         create_company_button = st.button("Adicionar Empresa", key="create_company")

# #         if create_company_button and st.session_state.lista:

# #             api_data = {
# #                 "company_id": id,
# #                 "company_name": company_name,
# #                 "prompt": prompt,
# #                 "urls": st.session_state.lista
# #             }

# #             try:
# #                 response = requests.post(ENDPOINT_URL + "/company", json=api_data, headers=HEADERS)
# #                 if response.status_code == 200:
# #                     st.success(f"Empresa '{company_name}' criada com sucesso!")
# #                 else:
# #                     st.error("Falha ao criar a empresa. Por favor, tente novamente.")
# #             except Exception as e:
# #                 st.error(f"Um erro ocorreu: {str(e)}")

# # elif st.session_state[PAGE_SELECTION_KEY] == "Atualize Empresa":
# #     st.title("🔄 Atualize Empresa")

# #     try:
# #         response = requests.get(ENDPOINT_URL + "/company", headers=HEADERS)
# #         if response.status_code == 200:
# #             companies = response.json()
# #             company_id_options = [company["name"] for company in companies]
# #         else:
# #             st.error("Falha ao obter a lista de empresas. Por favor, tente novamente.")
# #             st.stop()
# #     except Exception as e:
# #         st.error(f"Um erro ocorreu: {str(e)}")
# #         st.stop()

# #     selected_company_name = st.selectbox("Selecione a Empresa", company_id_options)

# #     selected_company_id = next(
# #         (company['id'] for company in companies if company["name"] == selected_company_name),
# #         None,
# #     )
    
# #     headers = {
# #         "content-type": "application/json",
# #         "x-api-key" : API_KEY
# #     }

# #     print("JORRRRGEEEE")
# #     option = st.radio("Escolha entre passar um documento ou uma lista de URLs", ("Documento", "Links"))

# #     if option == "Documento":
# #         document_type = st.selectbox("Tipo de Documento", ["csv", "pdf", "txt", "doc", "docx"])
# #         document_file = st.file_uploader("Upload", type=["csv", "pdf", "txt", "doc", "docx"])
    
# #     if document_file:
# #         document_name = str(document_file.name.rsplit('.', 1)[0])  # Nome do arquivo sem extensão
        
# #         update_company_button = st.button("Atualizar Empresa", key="update_company")

# #         print("id", selected_company_id, "documenttype:", document_type, "documentname: ", document_name)
# #         if update_company_button:
            
# #             # Solicita a URL assinada ao backend
# #             api_data = {
# #                 "id": selected_company_id,
# #                 "documentType": document_type,
# #                 "documentName": document_name,
# #                 "documentId": document_name  # Pode ajustar conforme necessário
# #             }
            
# #             print(api_data, headers)
# #             url_assinada_resposta = requests.post(f"{ENDPOINT_URL}/s3/signed-url", json=api_data, headers=headers)
# #             print(url_assinada_resposta)
# #             if url_assinada_resposta.status_code == 200:
# #                 url_assinada = url_assinada_resposta.json().get("uploadURL")

# #                 upload_resposta = requests.put(url_assinada, data=document_file)

# #                 if upload_resposta.status_code == 200:
# #                     st.success("Arquivo enviado com sucesso!")
# #                 else:
# #                     st.error(f"Erro ao enviar arquivo: {upload_resposta.text}")
# #             else:
# #                 st.error(f"Erro ao obter URL assinada: {url_assinada_resposta.text}")


# #     elif option == "Links":
# #         st.subheader("Lista de URLs")
# #         urls = st.text_input("Novo item")

# #         if "lista" not in st.session_state:
# #             st.session_state["lista"] = []

# #         if st.button('Adicionar'):
# #             if urls:
# #                 st.session_state.lista.append(urls)

# #         if st.session_state.lista:
# #             lista_str = "\n".join(st.session_state.lista)
# #             st.text_area("Itens da Lista", value=lista_str, height=200)

# #         update_company_button = st.button("Atualizar Empresa", key="update_company")

# #         if update_company_button and st.session_state.lista:

# #             api_data = {
# #                 "company_id": selected_company_id,
# #                 "prompt": prompt,
# #                 "urls": st.session_state.lista
# #             }

# #             try:
# #                 response = requests.post(ENDPOINT_URL + "/company", json=api_data, headers=HEADERS)
# #                 if response.status_code == 200:
# #                     st.success(f"Empresa '{selected_company_name}' atualizada com sucesso!")
# #                 else:
# #                     st.error("Falha ao atualizar a empresa. Por favor, tente novamente.")
# #             except Exception as e:
# #                 st.error(f"Um erro ocorreu: {str(e)}")

# # if st.session_state[PAGE_SELECTION_KEY] == "Empresas":
# #     st.title("🏢 Empresas")

# #     try:
# #         response = requests.get(ENDPOINT_URL + "/company", headers=HEADERS)
# #         if response.status_code == 200:
# #             data = response.json()
# #         else:
# #             st.error("Falha ao trazer empresas. Por favor, tente novamente.")
# #     except Exception as e:
# #         st.error(f"Um erro ocorreu: {str(e)}")

# #     if 'data' in locals():
# #         for i, company in enumerate(data):
# #             st.text_input(label='Company Name', value=company['name'], disabled=True, key=f"checkbox_{company['name']}-{i}")

# #             company_id = company['id']

# #             # Verificar se o campo 'sync' existe e é False
# #             if 'sync' in company and company['sync'] == False:
# #                 st.warning("Esta empresa ainda não foi sincronizada.")

# #             # try:
# #             #     response = requests.get(ENDPOINT_URL + f"/company/{company_id}")
# #             #     if response.status_code == 200:
# #             #         items = response.json()
# #             #     else:
# #             #         st.error("Falha ao trazer arquivos. Por favor, tente novamente.")
# #             # except Exception as e:
# #             #     st.error(f"Um erro ocorreu: {str(e)}")

# #             items = company['archives']

# #             if items is not None and items:
# #                 for i, archive in enumerate(company['archives']):
# #                     checkbox_selected = st.checkbox(f"🔗 {archive['archive_name']}", key=f"checkbox_{company_id}_{archive['archive_name']}-{i}")
# #                     if checkbox_selected:
# #                         selected_archives.append(archive['archive_name'])

# #                 delete_path = st.button("Excluir", key=f"delete_{company_id}_{i}")

# #                 if delete_path:
# #                     body = {
# #                         "paths": selected_archives
# #                     }
                    
# #                     try:
# #                         response = requests.post(ENDPOINT_URL + f"/company/{company_id}/delete", json=body, headers=HEADERS)
# #                         if response.status_code == 200:
# #                             st.success(f"Arquivo excluído com sucesso!")
# #                         else:
# #                             st.error("Falha ao excluir os arquivos. Por favor, tente novamente.")
# #                     except Exception as e:
# #                         st.error(f"Um erro ocorreu: {str(e)}")
# if st.session_state[PAGE_SELECTION_KEY] == "Chat":
#     st.title("💬 Inteligência de Embalagem 5.0")

#     # Obter empresas
#     try:
#         response = requests.get(ENDPOINT_URL + "/company", headers=HEADERS)
#         if response.status_code == 200:
#             companies = response.json()
#             company_id_options = [company["name"] for company in companies]
#         else:
#             st.error("Falha ao obter a lista de empresas. Por favor, tente novamente.")
#             st.stop()
#     except Exception as e:
#         st.error(f"Um erro ocorreu: {str(e)}")
#         st.stop()

#     # Seleção de empresa
#     selected_company_name = st.selectbox("Empresa", company_id_options)
#     selected_company_id = next(
#         (company['id'] for company in companies if company["name"] == selected_company_name),
#         None,
#     )

#     # Seleção de documento
#     selected_document_name = None
#     if selected_company_id:
#         try:
#             selected_company = next((company for company in companies if company["id"] == selected_company_id), None)
#             if selected_company and "archives" in selected_company:
#                 documents = selected_company["archives"]
#                 document_options = ["Todos os Documentos"] + [doc["archive_name"] for doc in documents]
#             else:
#                 st.error("Nenhum documento encontrado para esta empresa.")
#                 st.stop()
#         except Exception as e:
#             st.error(f"Erro ao carregar os arquivos: {str(e)}")
#             st.stop()

#     # # Dropdown para selecionar documento ou "Todos os Documentos"
#     # selected_document_name = st.selectbox("Documento", document_options)
#     # if selected_document_name == "Todos os Documentos":
#     #     selected_document_name = None  # Define como None para busca global

#     # Mostrar modelo e opções de chat
#     models = {
#         "claude-3-5-sonnet-v2": "us.anthropic.claude-3-5-sonnet-20241022-v2:0",
#     }

#     model_id_options = list(models.keys())
#     selected_model_id = st.selectbox("Modelo", model_id_options)
#     # show_citations = st.checkbox("Mostrar citações")

#     chosen_company_id = selected_company_id
#     chosen_model_id = models[selected_model_id]

#     # Mensagens do chat
#     if "messages" not in st.session_state:
#         st.session_state["messages"] = [
#             {"role": "assistant", "content": "Como posso ajudar você?"}
#         ]

#     for msg in st.session_state.messages:
#         st.chat_message(msg["role"]).write(msg["content"])

#     # Barra de entrada de texto aparece apenas na aba "Chat"
#     if prompt := st.chat_input():
#         # Adicionar a mensagem do usuário ao estado
#         user_message = {"role": "user", "content": prompt}
#         st.session_state.messages.append(user_message)

#         # Renderizar a mensagem do usuário imediatamente
#         st.chat_message("user").write(prompt)

#         # Construção do payload condicional
#         request_data = {
#             "question": prompt,
#             "companyId": chosen_company_id,
#             "modelId": chosen_model_id,
#         }
#         if selected_document_name:
#             request_data["document_id"] = selected_document_name

#         # Enviar requisição para a API
#         try:
#             response = requests.post(ENDPOINT_URL + "/chat", json=request_data, headers=HEADERS)
#             if response.status_code == 200:
#                 response_data = response.json()
#                 response_text = response_data["response"]

#                 # Adicionar a resposta ao estado
#                 assistant_message = {"role": "assistant", "content": response_text}
#                 st.session_state.messages.append(assistant_message)

#                 # Renderizar a resposta do assistente imediatamente
#                 st.chat_message("assistant").write(response_text)

#                 # if show_citations and "citation" in response_data:
#                 #     for citation_block in response_data["citation"]:
#                 #         citation_text = citation_block["content"]["text"]
#                 #         document_uri = citation_block["location"]["s3Location"]["uri"]
#                 #         document_name = citation_block["metadata"]["name"]

#                 #         st.markdown(f"**Citação do documento:** {document_name}")
#                 #         st.markdown(f"**URI do Documento:** {document_uri}")
#                 #         st.markdown(f"**Conteúdo:**\n{citation_text}")
#                 #         st.markdown("---")
#             else:
#                 st.error("Falhou em obter uma resposta da API.")
#         except Exception as e:
#             st.error(f"Ocorreu um erro ao tentar enviar o pedido.")



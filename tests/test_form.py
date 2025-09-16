from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicia o driver do Chrome
driver = webdriver.Chrome()
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 20)

    # Navega para a página principal
    driver.get("https://www.samsungsds.com/la/index.html")
    driver.save_screenshot("1_pagina_inicial.png")


    # Espera até que o ícone de contato seja clicável e o clica
    contact_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "floating_action")))
    contact_icon.click()

    # Espera a URL da página do formulário de contato ser carregada
    wait.until(EC.url_contains("contact_form.html"))
    driver.save_screenshot("2_pagina_do_formulario.png")


    # Dados para preencher o formulário
    test_data = {
        "name": "João da Silva",
        "company": "Minha Empresa S.A.",
        "email": "joao.silva@teste.com",
        "phone": "51999999999",
        "message": "Este é um teste de automação para o formulário de contato da Samsung SDS."
    }

    # **NOVO: Usa o ID correto para o campo "Nome"**
    full_name_field = wait.until(EC.visibility_of_element_located((By.ID, "field1")))
    full_name_field.send_keys(test_data["name"])

    # Preenche os demais campos de texto
    driver.find_element(By.ID, "field3").send_keys(test_data["company"])
    driver.find_element(By.ID, "field0").send_keys(test_data["email"])
    driver.find_element(By.ID, "field2").send_keys(test_data["phone"])
    driver.save_screenshot("3_campos_preenchidos.png")


    # Seleciona o radio button e os checkboxes
    radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*/div[1]/dl/dd[1]/label")))
    radio_button.click()
    driver.save_screenshot("4_radio_button_selecionado.png")


    checkbox_all = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Concordo com tudo.']")))
    checkbox_all.click()
    driver.save_screenshot("5_checkbox_all_selecionado.png")

    checkbox_email = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='E-mail']")))
    checkbox_email.click()
    driver.save_screenshot("6_checkbox_email_selecionados.png")

    # Preenche o campo de mensagem
    message_field = driver.find_element(By.NAME, "message")
    message_field.send_keys(test_data["message"])
    driver.save_screenshot("7_menssagem_escrita.png")

    # Clica no botão de enviar
    send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Enviar')]")
    send_button.click()

    # Espera até que a URL da página de sucesso seja carregada
    wait.until(EC.url_contains("thankyou.html"))

    # Valida a mensagem de sucesso na nova página
    success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Seu envio foi confirmado com sucesso.')]")))
    print("Teste de envio do formulário CONCLUÍDO com SUCESSO!")
    driver.save_screenshot("8_pagina_de_agradecimento.png")
    
    input("Pressione Enter para fechar o navegador...")

finally:
    driver.quit()

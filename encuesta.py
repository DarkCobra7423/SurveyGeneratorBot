import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Configurar el navegador con Selenium (en este caso, Firefox)
# driver = webdriver.Firefox(executable_path='/path/to/geckodriver')
num_repeticiones = 5

for _ in range(num_repeticiones):

    firefox_options = Options()
    driver = webdriver.Firefox(options=firefox_options)
    # Reemplaza con la URL de tu página
    driver.get(
        'https://survey.medallia.com/?ba-brick-qr&tienda=3571&negocio=3&formato=6&negocioOmni=3')

    def buttonNext():
        next = driver.find_element(By.ID, 'buttonNext')
        next.click()

    def buttonFinish():
        submit = driver.find_element(By.ID, 'buttonFinish')
        submit.click()

    # Ejecutar un script en JavaScript para llenar el formulario
    scriptPag1 = """
        async function slowTyping(element, text) {
        element.click(); // Asegurarse de que el elemento esté enfocado
        for (let character of text) {
            element.value += character;
            // Simular la entrada de texto con un pequeño retraso
            //await sleep(300); // Espera de 300 milisegundos (0.3 segundos)
        }
    }

    // Función de espera
    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    let razones = [
        "Precios bajos",
        "Productos de calidad",
        "Calidad en el servicio",
        "Buena Atencion",
        "Ofertas y promociones",
        "Cercania de la tienda"
    ]

    function rct() {
        var radioBoton = document.getElementById("onf_q_brick_ltr_gral_scale_9");
        if (radioBoton) {
            radioBoton.addEventListener('click', function () {
                // La función de callback se ejecuta cuando el clic es exitoso
                //alert("true");
                rprt();

            });
            radioBoton.click();
        } else {
            console.error("No se encontró el radio botón con el ID especificado.");
        }
    }

    function rprt() {
        setTimeout(async function () {
            //document.getElementById("spl_q_wm_brick_qr_ltr_gral_promotor_cmt").value = "Precios bajos"
            //await slowTyping(document.getElementById("spl_q_wm_brick_qr_ltr_gral_promotor_cmt"), razones[Math.floor(Math.random() * razones.length)]);
            await slowTyping(document.getElementById("spl_q_wm_brick_qr_ltr_gral_promotor_cmt"), razones[Math.floor(Math.random() * razones.length)]);
        }, 500);

    }
    rct();
    """

    scriptPag2 = """
    function ejecutarPag2() {
        //alert("ejecutando2")
        carniceria()
        recomendarCarniceria()
        principalRazon()
        masExperiencia()
    }

    function carniceria() {
        document.getElementById("onf_q_wm_brick_qr_deptos_carniceria_yn_1").click();
    }
    function recomendarCarniceria() {
        document.getElementById("onf_q_wm_brick_qr_carniceria_ltr_scale11_9").click();
    }

    function principalRazon() {
        document.getElementById("onf_q_wm_brick_qr_razon_promotor_carniceria_enum_7").click();

    }

    function masExperiencia() {
        document.getElementById("onf_q_wm_brick_qr_flex2_yn_1").click();
    }

    ejecutarPag2();
    """

    scriptPag3 = """
        function ejecutarPag3() {
        cajas(generarNumerosAleatorios())
        temperatura(generarNumerosAleatorios())
        amabilidad(generarNumerosAleatorios())
        entradaSalida(generarNumerosAleatorios())
        seguridad(generarNumerosAleatorios())
        instalaciones(generarNumerosAleatorios())
        facilidad(generarNumerosAleatorios())
        limpieza(generarNumerosAleatorios())
        iluminacion(generarNumerosAleatorios())
    }

    function generarNumerosAleatorios() {
        // Obtener un número aleatorio entre 8 y 10 (inclusive)
        const numeroAleatorio = Math.floor(Math.random() * 3) + 8;

        return numeroAleatorio;
    }

    function cajas(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_rappagocajas_scale11_" + num).click();
    }
    function temperatura(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_temp_scale11na_" + num).click();
    }
    function amabilidad(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_amabpersonal_scale11_" + num).click();
    }
    function entradaSalida(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_rapentradasalida_scale11_" + num).click();
    }
    function seguridad(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_seguridad_scale11_" + num).click();
    }
    function instalaciones(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_condgrles_scale11na_" + num).click();
    }
    function facilidad(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_facildesplaz_scale11_" + num).click();
    }
    function limpieza(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_limpieza_scale11na_" + num).click();
    }
    function iluminacion(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_ilum_scale11na_" + num).click();
    }

    ejecutarPag3();
    """

    scriptPag4 = """
    function ejecutarPag4() {
        estacionamiento(generarNumerosAleatorios())
        recibirAyuda(generarNumerosAleatorios())
        disponibilidadCalidad(generarNumerosAleatorios())
        limpiezaBaños(generarNumerosAleatorios())
        atencionClientes(generarNumerosAleatorios())
    }

    function generarNumerosAleatorios() {
        // Obtener un número aleatorio entre 8 y 10 (inclusive)
        const numeroAleatorio = Math.floor(Math.random() * 3) + 8;

        return numeroAleatorio;
    }

    function estacionamiento(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_estacionamiento_scale11na_" + num).click();
    }

    function recibirAyuda(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_encontrarpersonal_scale11na_" + num).click();
    }

    function disponibilidadCalidad(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_carritos_scale11na_" + num).click();
    }

    function limpiezaBaños(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_limpiezabanos_scale11na_" + num).click();
    }

    function atencionClientes(num) {
        document.getElementById("onf_q_wm_brick_qr_atributos_inf_atclientes_scale11na_" + num).click();
    }

    ejecutarPag4();
    """

    scriptPag5 = """
    function ejecutarPag5() {
        bodega()
        opinionAurrera()
        lugarMasComprado()
    }

    function bodega() {
        document.getElementById("onf_q_wm_brick_qr_lugar_3_meses_mas_gasto_enum_1").click();
    }
    function opinionAurrera() {
        document.getElementById("spl_q_wm_brick_qr_lugar_precios_bajos_cmt").value = "Mi bodega aurrera"
    }
    function lugarMasComprado() {
        document.getElementById("onf_q_wm_brick_qr_lugar_3_meses_bodegaa_yn_1").click();
    }

    ejecutarPag5();
    """

    scriptPag6 = """
    function participa() {
        document.getElementById("onf_q_wm_brick_qr_participar_dinamica_yn_2").click();
    }

    participa();
    """

    # Ejecutar el script
    driver.execute_script(scriptPag1)
    time.sleep(2)
    buttonNext()
    driver.execute_script(scriptPag2)
    time.sleep(1)
    buttonNext()
    driver.execute_script(scriptPag3)
    time.sleep(1)
    buttonNext()
    driver.execute_script(scriptPag4)
    time.sleep(1)
    buttonNext()
    driver.execute_script(scriptPag5)
    time.sleep(1)
    buttonNext()
    driver.execute_script(scriptPag6)
    time.sleep(1)
    buttonFinish()
    # Cerrar el navegador
    driver.quit()

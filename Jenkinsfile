node {

    stage("checkout repo") {
        git branch: 'master',
        credentialsId: '702ece7c-2044-4333-bdf9-8abee7fbb43f',
        url: 'https://github.com/PozhidaevYury/python-api-test.git'
    }

    stage("Test") {
        sh 'pytest tests -sv --alluredir=allure'
    }
}
pipeline {
    agent any

    parameters {
        choice(name: 'BROWSER', choices: ['chromium', 'firefox', 'webkit'], description: 'Оберіть браузер для тестів')
        string(name: 'BASIC_URL', defaultValue: 'https://qauto.forstudy.space', description: 'Base URL under test')
        string(name: 'USER_EMAIL', defaultValue: 'nedzelnytskyidev+hillel02026@gmail.com', description: 'Email користувача')
        password(name: 'USER_PASSWORD', defaultValue: 'AYf3JtDQnAcMbnc', description: 'Пароль користувача')
    }

    stages {
        stage('1: Git clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Hellrazers/hillel_courses.git'
            }
        }

        stage('2: Build Image') {
            steps {
                sh 'docker build -t ui-tests:latest .'
            }
        }

        stage('3: Run Tests') {
            steps {
                sh """
                    # Очищаємо робочі директорії
                    rm -rf allure-results ALLURE-RESULTS
                    mkdir -p allure-results ALLURE-RESULTS

                    # Видаляємо попередній контейнер, якщо він залишився
                    docker rm -f test_runner 2>/dev/null || true

                    # Запускаємо тести в іменованому контейнері без -v
                    docker run --name test_runner \\
                        -e BASIC_URL="${params.BASIC_URL}" \\
                        -e BASIC_AUTH_USER="guest" \\
                        -e BASIC_AUTH_PASS="welcome2qauto" \\
                        -e USER_LOGIN="${params.USER_EMAIL}" \\
                        -e USER_PASSWORD="${params.USER_PASSWORD}" \\
                        ui-tests:latest \\
                        pytest -m ${params.MARKS} --alluredir=allure-results --browser=${params.BROWSER} || true

                    # Копіюємо результати з контейнера у воркспейс Jenkins
                    docker cp test_runner:/app/allure-results/. allure-results/
                    docker cp test_runner:/app/allure-results/. ALLURE-RESULTS/

                    # Видаляємо контейнер після копіювання
                    docker rm -f test_runner
                """
            }
        }
    }

    post {
        always {
            allure([
                commandline: 'allure-results',
                includeProperties: false,
                jdk: '',
                results: [[path: 'allure-results'], [path: 'ALLURE-RESULTS']]
            ])
        }
    }
}
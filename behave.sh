#!/bin/bash

echo "开始执行Behave"

behave -f allure_behave.formatter:AllureFormatter -o report ./features

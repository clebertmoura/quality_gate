docker run \
    --rm \
    -e SONAR_HOST_URL="http://192.168.3.9:9000" \
    -e SONAR_LOGIN="sqp_de79ad241143394b9cc836f8d1577432367dcc41" \
    -v "./:/usr/src" \
    sonarsource/sonar-scanner-cli
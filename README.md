# Yandex_stt

virtualenv venv
source venv/bin/activate

pip install speechkit

export IAM_TOKEN=`yc iam create-token`
curl -H "Authorization: Bearer ${IAM_TOKEN}"   https://resource-manager.api.cloud.yandex.net/resource-manager/v1/clouds

export FOLDER_ID="b1g3ku6t41pjb00bids8"


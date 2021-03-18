echo $PASS
curl -X DELETE -u "apikey:$PASS" --verbose "$URL/v1/models/categories/$MODEL_ID?version=$VERSION"

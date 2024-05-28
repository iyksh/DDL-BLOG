#!/bin/bash
# verify if the script is executable:
# chmod +x run.sh

# Activate the virtual environment (Optional)
# source venv/bin/activate

# ================== Variables ==================

EXTERNAL_LIBRARIES=( 
  "django==3.2.4"
  "django-ckeditor-5==0.2.12"
)               

# ================== Functions ==================

start_server() {
  $1 manage.py runserver
  local status=$?
  if [ $status -eq 0 ]
  then
    echo "Server started successfully with $1."
  else
    echo "Server failed to start with $1."
  fi
  return $status
}

start_server_with_python() {
  start_server python
  if [ $? -ne 0 ]
  then
    start_server python3
  fi
}

install_libs(){
  for lib in "${EXTERNAL_LIBRARIES[@]}"
  do
    pip install $lib
    if [ $? -eq 0 ]
    then
      echo "Installed $lib successfully."
    else
      echo "Failed to install $lib."
    fi
  done
}

# ================== Main ==================

start_server_with_python

if [ $? -eq 0 ]
then
  echo "Server started successfully."
else
  echo "Server failed to start."
fi

install_libs
start_server_with_python
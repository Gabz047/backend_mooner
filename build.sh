set -o errexit
export PYTHONPATH=$PYTHONPATH:/opt/render/project/src/src
pip install --upgrade pip
pip install -r requirements.txt
python src/manage.py collectstatic --no-input
python src/manage.py migrate

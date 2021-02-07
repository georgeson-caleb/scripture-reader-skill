#Install postgres
echo "Installing postgres..."
sudo apt-get install -y postgresql

#Generate random password
echo "Generating credentials..."
password=`tr -dc A-Za-z0-9 </dev/urandom | head -c 25`

#Save username and password
echo "Saving credentials..."
echo "USER='scripture_reader'" | sudo tee /etc/scripture_reader_skill
echo "PASSWORD=$password" | sudo tee -a /etc/scripture_reader_skill

#Add user
echo "Creating user..."
sudo -u postgres psql -c "CREATE USER scripture_reader PASSWORD '$password'"

#Create the database
echo "Creating database..."
sudo -u postgres psql -c "CREATE DATABASE scriptures"
sudo -u postgres psql -d scriptures < lds-scriptures-postgresql.sql

#Give the user privileges for the database
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE scriptures TO scripture_reader"

echo "Database configuration completed."
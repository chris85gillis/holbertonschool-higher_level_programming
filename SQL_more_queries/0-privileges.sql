# Create 'user_0d_1' user and grant privileges
echo "CREATE USER 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p

# Create 'user_0d_2' user and grant privileges
echo "CREATE USER 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p
echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p

# List privileges for 'user_0d_1'
cat 0-privileges.sql | mysql -hlocalhost -uuser_0d_1 -p

# List privileges for 'user_0d_2'
cat 0-privileges.sql | mysql -hlocalhost -uuser_0d_2 -p
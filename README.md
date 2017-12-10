Install requirements

```
sh script/setup.sh
```

Run
```
sh script/run.sh
```

If a `*.ngrok.io` does not appear, try running the run script again. And make sure you're connected to the Internet. If you aren't then try going to `localhost:5000` on your browser.

If you're not in Ubuntu, or don't want to install the dependencies on your machine you can use vagrant. 
```
sudo apt-get install vagrant
vagrant up
vagrant ssh
cd /vagrant
sh script/setup.sh
sh script/run.sh
```
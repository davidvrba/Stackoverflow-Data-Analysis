# Stackoverflow-Data-Analysis
Analysis of Stackoverflow dataset

### Installation
1. Deploy EC2 instance in AWS cloud with a larger disk (200GB) and ssh to it from your terminal using
```
ssh -i key.pem ubuntu@<the ip address of your instance>
```

2. Clone the git repository and run the installation script that will install some packages, run the download script and finally uncompress the downloaded file
```
sudo apt-get install git
git clone https://github.com/davidvrba/Stackoverflow-Data-Analysis.git
chmod +x /home/ubuntu/Stackoverflow-Data-Analysis/installation.sh
sudo nohup /home/ubuntu/Stackoverflow-Data-Analysis/installation.sh
```
3. Open the Stackoverflow-Data-Analysis/src/data_upload_to_s3.py and fill in your S3 credentials (AccessKey, SecretKey, bucket). After that run the script
```
python3 Stackoverflow-Data-Analysis/src/data_upload_to_s3.py
```
It will upload the data to your S3 location.

4. Next start your EMR cluster and run the data-prepare/data-prepare notebook. This will convert the raw XML dataset to parquet and it will rename some columns.

5. Open the data-analysis/Posts-General-Analysis notebook on your EMR cluster and run the analysis.
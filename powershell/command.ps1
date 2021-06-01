##変数、関数を参照してくる
cd /tmp
. "./event_env.ps1"
. "./event_function.ps1"

mkdir $work_dir
aws ec2 describe-regions --region ap-northeast-1 >> $region_file
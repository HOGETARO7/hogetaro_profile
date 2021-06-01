#
# auto_shutdown.ps1
#
# 2021/02/18
#

###変数定義
#シャットダウン時に、切断したくないプロセスリスト
$FILEPATH1 = "./deny_list.txt"
$FILEPATH2 = "./ps_tmp.txt"
$FILEPATH3 = "./ps.txt"

###関数定義
function PsJudge ($Arg1) {
    if (!( $Arg1 -ge 1 )){

        $State = "Complete"

    }Else{

        Start-Sleep -Seconds 600
        $State = "NotYet"

}

###主処理

$Lists = Get-Content $FILEPATH1

foreach($List in $Lists){

    Write-Host $List

    Get-Process -Name $List > $FILEPATH2
    $COUNT = ( Get-Content $FILEPATH2 | Select-String $List ).Length

    PsJudge $COUNT

    if($State -contains "NotYet" ){
        PsJudge $COUNT
    }Else{
        $State = "Complete"
    }

}

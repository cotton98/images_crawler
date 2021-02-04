# images_crawler
944개의 이미지를 가져와야 함 -> 수작업으로 하나하나 하기는 효율성이 떨어짐 <br/>
크롤링 방법을 사용해서 가져옴 <br/>
준비된 데이터 셋 : movielens데이터의 poster url 저장 된 데이터 셋 <br/>
두개의 열로 준비된 데이터 셋에서 각 아이템마다 url만 긁어와서 크롤링 <br/>

##output.txt
준비된 데이터에는 서버에러난 url도 있고 누락된 itemid도 있어서 output.txt에 각 누락되거나 에러난 itemid저장 -> 이건 수작업으로 등록 예정

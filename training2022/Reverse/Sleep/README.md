Ý tưởng dựa trên thuật toán Sleep Sort, tuy nhiên thời gian Sleep đã bị thay đổi.

Để có được flag chỉ cần tìm đến API Sleep rồi sửa về thời gian gốc ban đầu

để được thứ tự sort đúng, sau đó xor đúng thứ tự trong mảng Key ban đầu

là thu được flag.

```
void SleepFunc(long long t){
	int temp = 66;
	if(t % 2 == 0){
		t = t * (temp * 2 + t % 10);
	}
	else{
		t = t * (temp) + temp/12;
	}
	t = t / 10000; // sua lai thanh t la co flag
	
	Sleep(t);
}
```

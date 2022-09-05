#include <iostream>
#include <string>
#include <windows.h>

using namespace std;

void TextColor(int x)
{
	HANDLE mau;
	mau = GetStdHandle(STD_OUTPUT_HANDLE);
	SetConsoleTextAttribute(mau,x);
}

int main()
{
	string flag1="ispclub{d0_y0u_l1k3_5ud0ku?}";
	string flag2="ispclub{l3t'5_try_4_puzzl3!}";
	string flag3="ispclub{y0u_d0_n0t_g3t_th3_fl4g}";
	string flag4="abcdefg{xxxxxxxxxxxxxxxxxxxxxxxxx}";
	string sudoku="haagaacadacaibaafaaafajcaaacaaahafaidahaajacaajaaeaaahbaiadhaacaaabaaiaagacaaajda";
	
	TextColor(2);
	cout << flag1 << endl;
	cout << "(Y or N)? ====> Answer: ";
	char answer;
	cin >> answer;
	cout << endl;
	
	if (answer=='Y' || answer=='y'){
		cout << flag2 << endl << endl;
		TextColor(4);
		int c=-1;
		for (int i=0; i<13; i++){
			for (int j=0; j<13; j++){
				if (i%4==0) cout << "--";
				else if (j%4==0) cout << "| ";
				else cout << sudoku[++c]-97 << " ";
			}
			cout << endl;
		}
		TextColor(14);
		flag4=flag1.substr(0, sudoku[2]-sudoku[13]) + flag1.substr(20, sudoku[72]-97) +  flag2.substr(19, sudoku[38]-97) + "_";
		flag4.push_back(sudoku[32]-49);
		flag4.push_back(sudoku[33]-49);
		flag4 += flag3.substr(sudoku[2]+sudoku[4]-97*2, sudoku[2]-sudoku[5]) + "345y}"; 
		
		if (flag4.size()==34) cout << flag4 << endl;
		else cout << "Try again";
	}
	else{
		TextColor(12);
		cout << flag3 << endl;
	}
	return 0;
}
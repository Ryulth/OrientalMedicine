#include <iostream>
#include <ctime>
#include <cstdlib>
#include <fstream>
#include <stdio.h>

using namespace std;

int* yunyang(int hua, int su, int mok, int kim, int to); // ������� ����ϴ� �Լ�, ����� ������ ���� ����

int main()
{
	
	srand((unsigned int)time(NULL));

	int num = 0;

	int hua = 0, su = 0, mok = 0, kim = 0, to = 0; // ȭ �� �� �� ��

	

	fstream DB; 

	DB.open("DB.txt"); // �������, �������(ȭ�������) 1916~2018������� ������


	int* result_;



	DB << "�������" << "   " << "ȭ" << " " << "��" << " " << "��" << " " << "��" << " " << "��" << endl;
	for (int year = 1916; year < 2019; year++) // 102�� , 1916����� 2018������� ������� �޷�
	{
		/////////////////

		cout << year << "��" << endl;

		int month = 1; // ��
		int day = 1; //��

		int February = 4;//����, �⺻������ 29�� ���޷� ����

		for (int month = 1; month < 13; month++)
		{
			cout << month << endl;
			if (month == 2)
			{
				if (February == 4)
				{
					for (int day = 1; day < 30; day++)
					{
						result_= yunyang(hua, su, mok, kim, to);
						hua= result_[0];
						su = result_[1];
						mok = result_[2];
						kim = result_[3];
						to = result_[4];
						DB << year  << month  << day << "   " << hua << " " << su << " " << mok << " " << kim << " " << to << endl;

					}
					February = 1; // ���� �Ǹ� �ٽ� ������ ����ϱ� ����

				}

				else
				{
					for (int day = 1; day < 29; day++)
					{
						cout << day << " ";

						result_ = yunyang(hua, su, mok, kim, to);
						hua = result_[0];
						su = result_[1];
						mok = result_[2];
						kim = result_[3];
						to = result_[4];

						DB << year << month << day << "   " << hua << " " << su << " " << mok << " " << kim << " " << to << endl;

					}
					February = February + 1; // 1�� ���������� 1�� ���ϰ��� 4���Ǹ� �����̵Ǵ� ��
				}


			}


			if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12)
			{
				cout << month << endl;
				for (int day = 1; day < 32; day++)
				{
					cout << day << " ";

					result_ = yunyang(hua, su, mok, kim, to);
					hua = result_[0];
					su = result_[1];
					mok = result_[2];
					kim = result_[3];
					to = result_[4];
					
					DB << year << month << day << "   " << hua << " " << su << " " << mok << " " << kim << " " << to << endl;

				}
				cout << endl;

			}


			else if (month == 4 || month == 6 || month == 9 || month == 11)
			{

				cout << month << endl;
				for (int day = 1; day < 31; day++)
				{
					cout << day << " ";

					result_ = yunyang(hua, su, mok, kim, to);
					hua = result_[0];
					su = result_[1];
					mok = result_[2];
					kim = result_[3];
					to = result_[4];
					DB << year << month << day << "   " << hua << " " << su << " " << mok << " " << kim << " " << to << endl;

				}
				cout << endl;
			}

			cout << endl;
		}

	}



	return 0;
}


int* yunyang(int hua,int su,int mok,int kim,int to)
{

	srand((unsigned int)time(NULL));


	//int hua = 0, su = 0, mok = 0, kim = 0, to = 0; // ȭ �� �� �� ��

	int num[3]; // �� ����� 3���� �����ִ�. ȭ �� �� �� �� �߿� 3��


	num[0] = 2; // ���� �ϳ��� ���� ���� 4���, ������ 6�̾�� �ϴ� �������� ���� 1�� ��
	num[1] = 2;
	num[2] = 2;


	int _num;

	_num = rand() % 5 + 1;


	if (_num==1)
	{
		hua = num[0];
		su = num[1];
		mok = num[2];
		kim = 0;
		to = 0;
	}

	else if (_num==2)
	{
		hua = num[0];
		su = 0;
		mok = num[2];
		kim = 0;
		to = num[1];
	}

	else if (_num == 3)
	{
		hua = num[0];
		su = num[1];
		mok = 0;
		kim = num[2];
		to = 0;
	}


	else if (_num == 4)
	{
		hua = 0;
		su = num[1];
		mok = num[2];
		kim = 0;
		to = num[0];
	}


	else if (_num == 5)
	{
		hua = 0;
		su = 0;
		mok = num[2];
		kim = num[1];
		to = num[0];
	}
	static int result[5];

	result[0] = hua;
	result[1] = su;
	result[2] = mok;
	result[3] = kim;
	result[4] = to;


	return result;

}

/*
int main()
{
	int Year, Mon;
	int M[12] = { 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	int Stand_Year = 0;
	int Start_One = 0;
	int Mon_One = 0;
	int r;
	printf("\n       -������ �Է��� �ּ��� : ");
	cin >> Year;
	printf("       -���� �Է��� �ּ���   : ");
	cin >> Mon;
	if (Year % 400 == 0 || (Year % 100 != 0 && Year % 4 == 0))
		M[1] = 29;
	else
		M[1] = 28;
	for (int i = 1900; i<Year; i++)
	{
		if (i % 400 == 0 || (i % 100 != 0 && i % 4 == 0))
		{
			Stand_Year = Stand_Year + 1;
		}
		Start_One = (Year - 1900 + Stand_Year) % 7 + 1;
	}
	if (Mon == 1)
		Start_One = Start_One;
	else
	{
		for (int j = 0; j<Mon - 1; j++)
		{
			Mon_One = Mon_One + M[j];
		}
		Start_One = (Start_One + Mon_One % 7) % 7;
	}
	printf("        ===================================================\n");
	printf("        Sun     Mon     The     Wed     Thu     Fri     Sat\n");
	for (int w = 0; w <= Start_One; w++)
	{
		printf("\t");
	}
	for (r = 1; r<8 - Start_One; r++)
	{
		printf(" %d\t", r);
	}
	printf("\n");
	for (int t = 0; t<5; t++)
	{
		puts("\n");
		for (int u = 0; u<7; u++)
		{
			if (r <= M[Mon - 1])
			{
				printf("\t %d", r);
				r = r + 1;
			}
			else
			{
				puts("\n        ===================================================\n");
				return 0;
			}
		}
		printf("\n");
	}

}
*/
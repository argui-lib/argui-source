#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

int main(int argc, char**argv){
	// argc is the argument count
	// argv is a list of arguments
	// argv always has filename as first argument
	// argv then has user defined arguments
	int i;
	for (i = 0;i < argc; i++){
		//cout << argv[i] << endl;
		printf("%s\n", argv[i]);
	}
	return 0;
}


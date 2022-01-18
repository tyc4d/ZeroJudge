#include <iostream>
#include <string>
using namespace std;

static const auto Initialize = [] {
	cin.sync_with_stdio(false); cin.tie(nullptr);
	return nullptr;
}();

string Reverse(string text) {
	string buffer = "";
	for (int i = text.size() - 1; i >= 0; --i)
		buffer += text[i];
	return buffer;
}

int main() {
	int last;
	bool direction;
	string ciphered;
	while (cin >> ciphered) {
		last = direction = false;
		for (int i = 0; i != ciphered.size(); ++i)
			if (ciphered[i] == '+' || ciphered[i] == '-') {
				cout << (direction ? Reverse(ciphered.substr(last, i - last)) : ciphered.substr(last, i - last));
				direction = (ciphered[i] == '-');
				last = i + 1;
			}
		if (last != ciphered.size())
			cout << (direction ? Reverse(ciphered.substr(last)) : ciphered.substr(last));
		cout << '\n';
	}
}
#include "hamming.h"
#include <string>
using namespace std;

namespace hamming {
    
    int compute (const char* input1, const char* input2) {
        string strand1 = input1;
        string strand2 = input2;
        int distance = 0;

        if (strand1.length() != strand2.length()) {
            distance = -1;
        } else {
            for (unsigned int i = 0; i < strand1.length(); i++) {
                if (strand1[i] != strand2[i]) {
                    distance++;
                }
            }
        }

        return distance;
    }
}  // namespace hamming

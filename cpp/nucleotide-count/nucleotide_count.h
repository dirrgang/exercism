#if !defined(NUCLEOTIDE_COUNT_H)
#define NUCLEOTIDE_COUNT_H
#include <string>
#include <map>

using namespace std;

namespace nucleotide_count
{

class counter
{
private:
    /* data */
    string dna_string;

public:
    counter(string derp);
    ~counter();

    map<char, int> nucleotide_counts();
};

} // namespace nucleotide_count

#endif // NUCLEOTIDE_COUNT_H
#include <Python.h>

class TestFact{
public:
    TestFact(){};
    ~TestFact(){};
    int fact(int n);
};

int TestFact::fact(int n)
{
    if (n <= 1)
        return 1;
    else
        return n * (n - 1);
}

extern "C"
int fact(int n)
{
    TestFact t;
    return t.fact(n);
}

#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;
const long long INF = 2e18;
const long long BIGGEST = (1LL << 31) - 1;

long int int_log(long long a)
{
    long long max_pow, k;
    
    if (a <= 1)
    {
        return 0;
    }
    
    max_pow = 2;
    k = 1;
    while (max_pow < a)
    {
        max_pow *= 2;
        k++;
    }
    return k;
}

class SegmentTree
{
private:
    long int size, len, orig_len;
    long long* tree;
    long long* upd;
    bool* is_final;
    
    long long get(long int v)
    {
        return tree[v] + upd[v];
    }
    
    void push(long int v, long int l, long int r)
    {
        if (l == r)
        {
            tree[v] += upd[v];
            is_final[v] = false;
        }
        else
        {
            if (is_final[v] == true)
            {
                tree[v] += upd[v];
                tree[2 * v + 1] = tree[v];
                tree[2 * v + 2] = tree[v];
                upd[2 * v + 1] = 0;
                upd[2 * v + 2] = 0;
                is_final[v] = false;
                is_final[2 * v + 1] = true;
                is_final[2 * v + 2] = true;
            }
            else
            {
                upd[2 * v + 1] += upd[v];
                upd[2 * v + 2] += upd[v];
                if (get(2 * v + 1) <= get(2 * v + 2))
                {
                    tree[v] = get(2 * v + 1);
                }
                else
                {
                    tree[v] = get(2 * v + 2);
                }
            }
        }
        upd[v] = 0;
        return;
    }
    
    long long rmq_back(long int v, long int l, long int r, long int a, long int b) 
    {
        //Backend function for RMQ
        long int m;
        long long v1, v2;
        push(v, l, r);
        if (l > b || r < a)
        {
            return INF;
        }
        if (l >= a && r <= b)
        {
            return get(v);
        }
        m = (l + r) / 2;
        v1 = rmq_back(2 * v + 1, l, m, a, b);
        v2 = rmq_back(2 * v + 2, m + 1, r, a, b);
        if (v1 <= v2)
        {
            return v1;
        }
        else
        {
            return v2;
        }
    }
    
    void update_back(long int v, long int l, long int r, long int a, long int b, long long x)
    {
        //Backend function for Update
        long int m;
        long long v1, v2;
        push(v, l, r);
        if (l > b || r < a)
        {
            return;
        }
        if (l >= a && r <= b)
        {
            upd[v] += x;
        }
        else
        {
            m = (l + r) / 2;
            update_back(2 * v + 1, l, m, a, b, x);
            update_back(2 * v + 2, m + 1, r, a, b, x);
            v1 = get(2 * v + 1);
            v2 = get(2 * v + 2);
            if (v1 <= v2)
            {
                tree[v] = v1;
            }
            else
            {
                tree[v] = v2;
            }
        }
        
    }
    
    void set_back(long int v, long int l, long int r, long int a, long int b, long long x)
    {
        //Backend function for set
        long int m;
        long long v1, v2;
        push(v, l, r);
        if (l > b || r < a)
        {
            return;
        }
        if (l >= a && r <= b)
        {
            tree[v] = x;
            is_final[v] = true;
        }
        else
        {
            m = (l + r) /2;
            set_back(2 * v + 1, l, m, a, b, x);
            set_back(2 * v + 2, m + 1, r, a, b, x);
            v1 = get(2 * v + 1);
            v2 = get(2 * v + 2);
            if (v1 <= v2)
            {
                tree[v] = v1;
            }
            else
            {
                tree[v] = v2;
            }
        }
    }
    
public:

    SegmentTree(long long* array, long int n)
    {
        long int log_n;
        long int i, idx;
        
        orig_len = n;
        log_n = int_log(n);
        size = (1 << (log_n + 1)) - 1;
        len = 1 << log_n;
        
        tree = new long long[size];
        upd = new long long[size];
        is_final = new bool[size];
        
        idx = 1;
        while (idx < n)
        {
            idx *= 2;
        }
        
        for (i = 0; i < size; i++)
        {
            tree[i] = INF;
            upd[i] = 0;
            is_final[i] = false;
        }
        for (i = 0; i < n; i++)
        {
            tree[idx + i - 1] = array[i];
            //printf("%lld %lld\n", tree[idx + i -1], array[i]);
        }
        for (i = idx - 2; i >= 0; i--)
        {
            if (tree[2 * i + 1] <= tree[2 * i + 2])
            {
                tree[i] = tree[2 * i + 1];
            }
            else
            {
                tree[i] = tree[2 * i + 2];
            }
        }
        //p_d("INI");
    }
    
    ~SegmentTree()
    {
        delete tree;
        delete upd;
        delete is_final;
    }
    
    long long rmq(long int a, long int b)
    {
        return rmq_back(0, 0, len - 1, a, b);
    }
    
    void update(long int a, long int b, long long x)
    {
        update_back(0, 0, len - 1, a, b, x);
    }
    
    void set(long int a, long int b, long long x)
    {
        set_back(0, 0, len - 1, a, b, x);
    }
    
    void return_tree(long long* a)
    {
        long i;
        for (i = 0; i < orig_len; i++)
        {
            a[i] = rmq(i, i);
        }
    }
    
    void p_d(char* message) 
    {
        //For debug - prints internal structure
        int i;
        printf("%s\n", message);
        for (i = 0; i < size; i++)
        {
            printf("%lld %lld %d\n", tree[i], upd[i], is_final[i]);
        }
    }
};

int check_req(vector<vector<long long>> & req, long long* res, long n, long m)
{
    long i, j;
    SegmentTree* st;
    sort(req.begin(), req.end());
    
    for (i = 0; i < n; i++)
    {
        res[i] = INF;
    }
    
    st = new SegmentTree(res, n);
    for (i = 0; i < m; i++)
    {
        st->set(req[i][1] - 1, req[i][2] - 1, req[i][0]);
    }
    for (i = 0; i < m; i++)
    {
        if (st->rmq(req[i][1] - 1, req[i][2] - 1) != req[i][0])
        {
            delete st;
            return -1;
        }
    }
    
    st->return_tree(res);
    delete st;
    return 0;
}

int main()
{
    long long n, m, a, b, i, j;
    long long* array;
    long long x;
    vector <vector <long long>> req;
    vector <long long> tmp;
    FILE* fin;
    FILE* fout;
    
    fin = fopen("rmq.in", "r");
    fout = fopen("rmq.out", "w");
    
    fscanf(fin, "%lld%lld", &n, &m);
    for (i = 0; i < m; i++)
    {
        fscanf(fin, "%lld%lld%lld", &a, &b, &x);
        tmp = {x, a, b};
        req.push_back(tmp);
    }
    
    array = new long long[n];

    x = check_req(req, array, n, m);
    if (x < 0)
    {
        fprintf(fout, "inconsistent\n");
    }
    else
    {
        fprintf(fout, "consistent\n");
        for (i = 0; i < n; i++)
        {
            if (array[i] < INF)
            {
                fprintf(fout, "%lld ", array[i]);
            }
            else
            {
                fprintf(fout, "%lld ", BIGGEST);
            }
        }
    }
    
    fclose(fin);
    fclose(fout);
    delete array;
    return 0;
}

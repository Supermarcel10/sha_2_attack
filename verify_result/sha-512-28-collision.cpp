/**
 * SHA-256 implemented according to the specification:
 * http://csrc.nist.gov/publications/fips/fips180-4/fips-180-4.pdf
 */
#include <iomanip>
#include <iostream>
#include <cstdint>
#include <vector>

// Constants used in hash algorithm
const uint64_t K[] = {0x428a2f98d728ae22, 0x7137449123ef65cd, 0xb5c0fbcfec4d3b2f, 0xe9b5dba58189dbbc, 0x3956c25bf348b538, 0x59f111f1b605d019, 0x923f82a4af194f9b, 0xab1c5ed5da6d8118,
                      0xd807aa98a3030242, 0x12835b0145706fbe, 0x243185be4ee4b28c, 0x550c7dc3d5ffb4e2, 0x72be5d74f27b896f, 0x80deb1fe3b1696b1, 0x9bdc06a725c71235, 0xc19bf174cf692694,
                      0xe49b69c19ef14ad2, 0xefbe4786384f25e3, 0x0fc19dc68b8cd5b5, 0x240ca1cc77ac9c65, 0x2de92c6f592b0275, 0x4a7484aa6ea6e483, 0x5cb0a9dcbd41fbd4, 0x76f988da831153b5,
                      0x983e5152ee66dfab, 0xa831c66d2db43210, 0xb00327c898fb213f, 0xbf597fc7beef0ee4, 0xc6e00bf33da88fc2, 0xd5a79147930aa725, 0x06ca6351e003826f, 0x142929670a0e6e70,
                      0x27b70a8546d22ffc, 0x2e1b21385c26c926, 0x4d2c6dfc5ac42aed, 0x53380d139d95b3df, 0x650a73548baf63de, 0x766a0abb3c77b2a8, 0x81c2c92e47edaee6, 0x92722c851482353b,
                      0xa2bfe8a14cf10364, 0xa81a664bbc423001, 0xc24b8b70d0f89791, 0xc76c51a30654be30, 0xd192e819d6ef5218, 0xd69906245565a910, 0xf40e35855771202a, 0x106aa07032bbd1b8,
                      0x19a4c116b8d2d0c8, 0x1e376c085141ab53, 0x2748774cdf8eeb99, 0x34b0bcb5e19b48a8, 0x391c0cb3c5c95a63, 0x4ed8aa4ae3418acb, 0x5b9cca4f7763e373, 0x682e6ff3d6b2b8a3,
                      0x748f82ee5defb2fc, 0x78a5636f43172f60, 0x84c87814a1f0ab72, 0x8cc702081a6439ec, 0x90befffa23631e28, 0xa4506cebde82bde9, 0xbef9a3f7b2c67915, 0xc67178f2e372532b,
                      0xca273eceea26619c, 0xd186b8c721c0c207, 0xeada7dd6cde0eb1e, 0xf57d4f7fee6ed178, 0x06f067aa72176fba, 0x0a637dc5a2c898a6, 0x113f9804bef90dae, 0x1b710b35131c471b,
                      0x28db77f523047d84, 0x32caab7b40c72493, 0x3c9ebe0a15c9bebc, 0x431d67c49c100d4c, 0x4cc5d4becb3e42b6, 0x597f299cfc657e2a, 0x5fcb6fab3ad6faec, 0x6c44198c4a475817};

// std::vector<WORD> M;              // Message to be hashed
std::vector<uint64_t> H; // Hashed message

uint64_t W[80]; // Message schedule

uint64_t hash_block[8];
// Working variables
uint64_t a, b, c, d, e, f, g, h;

// Temporary words
uint64_t T1, T2;

/**
 * Take the given hexadecimal string and store the bytes in a global vector.
 * Also update the message length.
 */

/**
 * Initialise the hash value H_0.
 */
const void init_hash(uint64_t h0[])
{

    H.push_back(h0[0]);
    H.push_back(h0[1]);
    H.push_back(h0[2]);
    H.push_back(h0[3]);
    H.push_back(h0[4]);
    H.push_back(h0[5]);
    H.push_back(h0[6]);
    H.push_back(h0[7]);
}

/**
 * Rotate right function ROTR^n(x) in hash algorithm.
 */
const uint64_t ROTR(const uint64_t &n, const uint64_t &x)
{
    return (x >> n) | (x << (64 - n));
}

/**
 * Right shift function SHR^n(x) in hash algorithm.
 */
const uint64_t SHR(const uint64_t &n, const uint64_t &x)
{
    return x >> n;
}

/**
 * Logical function Ch(x, y, z) in hash algorithm.
 */
const uint64_t Ch(const uint64_t &x, const uint64_t &y, const uint64_t &z)
{
    return (x & y) ^ (~x & z);
}

/**
 * Logical function Maj(x, y, z) in hash algorithm.
 */
const uint64_t Maj(const uint64_t &x, const uint64_t &y, const uint64_t &z)
{
    return (x & y) ^ (x & z) ^ (y & z);
}

/**
 * Logical function (large) sigma^256_0(x) in hash algorithm.
 */
const uint64_t lsigma0(const uint64_t &x)
{
    return ROTR(28, x) ^ ROTR(34, x) ^ ROTR(39, x);
}

/**
 * Logical function (large) sigma^256_1(x) in hash algorithm.
 */
const uint64_t lsigma1(const uint64_t &x)
{
    return ROTR(14, x) ^ ROTR(18, x) ^ ROTR(41, x);
}

/**
 * Logical function (small) sigma^256_0(x) in hash algorithm.
 */
const uint64_t ssigma0(const uint64_t &x)
{
    return ROTR(1, x) ^ ROTR(8, x) ^ SHR(7, x);
}

/**
 * Logical function (small) sigma^256_1(x) in hash algorithm.
 */
const uint64_t ssigma1(const uint64_t &x)
{
    return ROTR(19, x) ^ ROTR(61, x) ^ SHR(6, x);
}

/**
 * Compute the hash value.
 */
const void compute_hash(std::vector<uint64_t> M)
{
    for (int t = 0; t <= 15; ++t)
        W[t] = M[t]; // M^i in spec
    for (int t = 16; t <= 80; ++t)
        W[t] = ssigma1(W[t - 2]) + W[t - 7] + ssigma0(W[t - 15]) + W[t - 16];

    // Initialise working variables with previous hash value
    a = H[0];
    b = H[1];
    c = H[2];
    d = H[3];
    e = H[4];
    f = H[5];
    g = H[6];
    h = H[7];

    // Perform logical operations
    for (int t = 0; t <= 27; ++t)
    {
        T1 = h + lsigma1(e) + Ch(e, f, g) + K[t] + W[t];

        T2 = lsigma0(a) + Maj(a, b, c);

        h = g;

        g = f;
        f = e;
        e = d + T1;
        d = c;
        c = b;
        b = a;
        a = T1 + T2;
    }

    // Compute intermediate hash values by assigning them to H^i

    hash_block[0] = (a + H[0]);
    hash_block[1] = (b + H[1]);
    hash_block[2] = (c + H[2]);
    hash_block[3] = (d + H[3]);
    hash_block[4] = (e + H[4]);
    hash_block[5] = (f + H[5]);
    hash_block[6] = (g + H[6]);
    hash_block[7] = (h + H[7]);
}

/**
 * Output the generated hash value as a hexadecimal string.
 */
const void output_hash()
{
    // Concatenate the final hash blocks
    for (int i = 0; i < 8; ++i)
        std::cout << std::hex << std::setw(16) << std::setfill('0') << hash_block[i] << " ";
    std::cout << std::endl;
}

int main()
{
    uint64_t h0[] = {0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
                     0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b, 0x5be0cd19137e2179};
    std::vector<uint64_t> W0;

    W0.push_back(0x1f736d69a0368ef6);
    W0.push_back(0x7277e5081ad1c198);
    W0.push_back(0xe953a3cdc4cbe577);
    W0.push_back(0xbd05f6a203b2f75f);
    W0.push_back(0xdd18b3e39f563fca);
    W0.push_back(0xcad0a5bb69049fcd);
    W0.push_back(0x4d0dd2a06e2efdc0);
    W0.push_back(0x86db19c26fc2e1cf);
    W0.push_back(0x184949e92cdd314);
    W0.push_back(0x82fb3c1420112000);
    W0.push_back(0xe4930d9b8295ab26);
    W0.push_back(0x5500d3a2f30a3402);
    W0.push_back(0x26f0aa8790cb1813);
    W0.push_back(0xa9c09c5c5015bc0d);
    W0.push_back(0x53892c5a64e94edb);
    W0.push_back(0x8e60d500013a1932);

    // Set the inital hash value
    init_hash(h0);

    // Compute the hash value
    compute_hash(W0);

    // Output the generated hash value
    output_hash();

    std::vector<uint64_t> W1;

    W1.push_back(0x1f736d69a0368ef6);
    W1.push_back(0x7277e5081ad1c198);
    W1.push_back(0xe953a3cdc4cbe577);
    W1.push_back(0xbd05f6a203b2f75f);
    W1.push_back(0xdd18b3e39f563fca);
    W1.push_back(0xcad0a5bb69049fcd);
    W1.push_back(0x4d0dd2a06e2efdc0);
    W1.push_back(0x86db19c26fc2e1cf);
    W1.push_back(0x37a8f464c0bb995);
    W1.push_back(0x83033bd41e111fff);
    W1.push_back(0xe4930d9b8295ab26);
    W1.push_back(0x5500d3a2f30a3402);
    W1.push_back(0x26f0aa8790cb1813);
    W1.push_back(0xa9809e5c4015bc45);
    W1.push_back(0x53892c5a64e94edb);
    W1.push_back(0x8e60d500013a1932);

    // Compute the hash value
    compute_hash(W1);

    // Output the generated hash value
    output_hash();
}
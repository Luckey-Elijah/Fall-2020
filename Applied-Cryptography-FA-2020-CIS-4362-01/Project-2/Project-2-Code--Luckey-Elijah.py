ASCII = "ASCII"
UTF_8 = "utf-8"
HEX = "hex"
LATIN_1 = 'latin-1'

# FREQ_WORDS = ["the"]
FREQ_WORDS = [
    "the", "of", "and", "a", "to", "in", "is", "be", "that", "was", "he",
    "for", "it", "with", "as", "his", "I", "on", "have", "at", "by", "not",
    "they", "this", "had", "are", "but", "from", "or", "she"
]

TESTS = [
    "866e786a0042d4abf21e305c35ad65c1b542bbbe8f55b3848032c6359fc3e2e96b21421196a107c90195a30896bc61f54906abae35fd196fb1519b2d1206320b892b7c7719e60e37b697738c0776292a9c5d132ac66a8bd1a728bb5882e629",
    "9c647079135f94eef80265133bec67ccf006b3bc8944a69d84228f2296cae2e962364a069ba111c91188e34ccfb27af5400bbaa467f20469b50ed33c1e436601897869240be30e36a99b6990442561249e5d1327c170d8dce638f35f83a866f9ca08b8f05f0123856491c68b56b91dad9d6b2c4a6315238b2316c88b51c7fbbcd50f9ee7fbc66ccad06febb77070e92c3eb292befb613250bf2c69a3e40a3410959a14630e9d5219e780828c81ca1d766cc0f811",
    "9d64746a044fd8e0ee08651f2fb563d0fa41acbc8d44bad08833922998c2b1bd6f3e55188df853cd5992e44688bf71f54a02a4eb73f40221ba4d8720564328009e726d7003e00779ba9c79d84d3322379548473ac67185",
    "876f377f04559df9ea1d695c2db971c8fc45feb69855e393972f963598c1b0fc7a3b5c5491f800d81c8cfe089aa071f54906afaf38ef1f2cab4d9f3e130636118369716107fc4938a8d269904c7623249f514073c6798bcdae29bb5f9bef68f9c65ca7f81d4d5a866fdedc8a05ac53b9cf792d49625129852e17858f53d4f1aa9c1993e9bac770cb9162a3b46622a82e2ef09fbbeb2e7942a36066fce91f330b978c557208805207f1cc9cd29392487064d6f95ba8862fea642eabf3c8f2227f5e25bc74e35386a6d6748cafe75c320c7c04a7bfef57b4fa799b6baf1d06834901",
    "9a6972380c5a91e5f80537193ca133c7e75faea9924bb191953e8f22d7c5adf067264b1d96f853c41892ad4480bd73f54902b1af35ef1860ac02972d05013543d93d306603fb4932be8b3d8f4825613183571320c170d9cde638f41e80e173e3dc5caefb574d6fce688cc49113f515a6cf7f2c066e4c3385230885884ddcf3f898029fe1e8dd3fcc9f76f3a77d35fa2d75b281b7e56b7f45bf3225e3ff003501d78d146e018e484ee18383d187ca0d6025d5f348ed9b61ae7f33acbfddf36b774d60a86ca016d1f4c83b8dbdaf59795e624dbdbbf310a5b271813fa31400835f4eec250ddd43de10a25e790c9f28e7ebd0c74fa11181fcf79cf68d5bd75b662bbacf38d31b39cbcdc71d213d611812188ebe8855dcf857337ac75e2b36cceb0c4a729e1b7c72e78e0962c112351e62aa0f41456ebd34667929cdb06c2ffd627d7b11da0b6dd57900d0cafd9651a32e8d4247a7ab3cce24d08150ceee321b38dae50481acf00896ce1f8c7b7499dcf79008c9b5aee24b8de4ff1737116c",
    "8f2175740e5893abe818351438be33cde606adb2d04fa29c8933826195c3a1fc7f20405496e9168c0a82e54d82b634b04f04afb265ef0321b74c9668144a2900872b72624aeb082dbad27c8c0937613185555673dc6cc2d7a16cef5692a874eac24deffe56142e8164ded48415b053abd1732a4d21",
    "9a697e6b415897fef902205c34a267d6fa42abbe985fe393972f963598c1b0fc7a3b4c17c2f101c51488f94199b667f54009b9eb7df40721ac4a963156473406cc62707406ea043cb586789c093f2f658d48433fc07ccacdaf23f54dd9a853e4df41ace6130e61986f8cd48156b11daad1692d433518349d2d0ec09a4ddafdf59e0882a4ffdd7cdd896bf7bb663ea83f37f59ca0e17a7a4aa96c25fee50d2b0d93de5f6719d91700e19e97d186d7077c2985f856ef8035ab7c66bdbadfee2a664e77bf66ac0788bac1748eacb45936196004a2b0e955b6a8798166e4",
    "8a68717e085ed8eae515651438a07fc9f448feb49358b19f812385249386b6f56f73461b8ce216dc0dc1e24ecfa361b74d0ebeeb7efe0921bb508a38024921118d7b757d44af1d31bed270995d3e24288d4c5a30c8738b9bb23ef25d9caa27e4c908abfc550b678b2796d4891ab512a79d772c5f2f5d3f872802cb895a93f7abd51993e5ee9376dbd072f0f27b35e43f2ffb85b7e4773242bb337caee40067079f934477149c520bfa9c81cf97d01c6125c6f352f88833af7466babc98e3247f4b70ae7cee40c9b0cc2780bba25e325e694bacbfef59a5b27d8631",
    "9d6e7a7d155295eef8512c087da56084f743aaa9985ee3848a768c3484d2e2ea6b3f4e5483f612d55987ff4782f360bd4809bab835fa1e65f8459c6814472508cc7f72241ee70c34fb9e7c8c4c246132845d5d73d070de99a73efe1e9ee627ea8f4aaae147087cce6c8cd08813f81caf9d7120486b16",
    "8968617d0f1b97e5ee51280f3aec72caf106bdb48d44a68291339e35db86b6f56f2140548bf253cd1593e8498baa34ba4f02fda070e25075b04387681b473610cc7f75614ae21a3efb8672d85d3e2031cc5b5a23c17ad9cda334ef10",
]

TARGET = "8f6f3779154f99e8e014375c34a267c1e745bbad895fe391c526873383cfa1e86632575481e803c41c93f94d97a738f54d02a9ec66bb1360b44ed3210206254fcc627b240bfb1d38b899788a093d2f2a9b4b1327c17edf99b224fe1e9ee66effc649a3b5430c7c9a2a91d7c51bab14e9d57d39566a5634c4340c858c5a93fff89e0394f3f49369ce9c6ee6f26b29a82e29fb9ca0a8657c48ad2c60eaf70a6b44918a40630392171ca29b87cd9e9e037c6ad2bc4be08c61ba6223a8bac0a024741b71b270a0579ab1d0308ce9b54b391a6a49ebacfc5eb5b57dd56caf0b1694544cfa6e"


def string_xor(a: str, b: str) -> hex:
    """
    Performs XOR of two full length strings.
    Assuming the strings are base-16.
    """

    # String lengths
    a_len: int = len(a)
    b_len: int = len(b)

    # Assertion
    if a_len < 1 or b_len < 1:
        raise AssertionError("Length is less than 1.")

    if a_len > b_len:
        # slice a
        a = a[0:b_len]
        a_len = len(a)
    elif b_len > a_len:
        # slice b
        b = b[0:a_len]
        b_len = len(b)

    return hex(int(a, base=16) ^ int(b, base=16))


if __name__ == "__main__":

    xored_list = []

    # xor each case against each other
    for i in range(len(TESTS)):
        for j in range(i):
            x = string_xor(TESTS[i], TESTS[j])
            x_stripped = x[2:]
            xored_list.append(x_stripped)

    cribs = []

    # For every xor message, try each of the FREQ_WORDS items for crib dragging
    for xor_list_i in range(len(xored_list)):

        # pick asimple to crib drag against
        xor_hex_sample = xored_list[xor_list_i]

        # For all the 30 words in the list, crib drag across the xor sample
        for word_i in range(len(FREQ_WORDS)):

            # convert the word to hex
            word_hex_as_str = FREQ_WORDS[word_i].encode(UTF_8).hex()

            crib = ""
            word_hex_as_str_len = len(word_hex_as_str)
            iterations = len(xor_hex_sample) - len(word_hex_as_str)

            # populate the crib string
            for xor_index in range(iterations):
                xor_slice = xor_hex_sample[xor_index: xor_index +
                                           word_hex_as_str_len]

                c = string_xor(word_hex_as_str, xor_slice)[2:]

                # add padding to hex
                if len(c) % 2 != 0:
                    c = '0' + c

                # Convert c -> ascii
                byte = bytes.fromhex(c)
                c_decoded = byte.decode(LATIN_1)

                # add it to the list
                crib = crib + c_decoded

            # update the cribs
            cribs.append(crib)

    # Logic: search across the cribs for matches
    count: int = 0
    for crib in cribs:
        for word in FREQ_WORDS:
            if word in crib:
                count += 1
                print("Found match \"{}\"".format(word))
    print(count)

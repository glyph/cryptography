# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

INCLUDES = """
#include <openssl/bn.h>
"""

TYPES = """
typedef ... BIGNUM;
/*
 * TODO: This typedef is wrong.
 *
 * This is due to limitations of cffi.
 * See https://bitbucket.org/cffi/cffi/issue/69
 *
 * For another possible work-around (not used here because it involves more
 * complicated use of the cffi API which falls outside the general pattern used
 * by this package), see
 * http://paste.pound-python.org/show/iJcTUMkKeBeS6yXpZWUU/
 *
 * The work-around used here is to just be sure to declare a type that is at
 * least as large as the real type.  Maciej explains:
 *
 * <fijal> I think you want to declare your value too large (e.g. long)
 * <fijal> that way you'll never pass garbage
 */
typedef uintptr_t BN_ULONG;
"""

FUNCTIONS = """
BIGNUM *BN_new(void);
void BN_free(BIGNUM *);

int BN_set_word(BIGNUM *, BN_ULONG);

char *BN_bn2hex(const BIGNUM *);
int BN_hex2bn(BIGNUM **, const char *);
int BN_dec2bn(BIGNUM **, const char *);

int BN_num_bits(const BIGNUM *);
"""

MACROS = """
"""

CUSTOMIZATIONS = """
"""

CONDITIONAL_NAMES = {}

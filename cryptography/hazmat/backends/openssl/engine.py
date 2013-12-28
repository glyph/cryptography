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
#include <openssl/engine.h>
"""

TYPES = """
typedef ... ENGINE;
"""

FUNCTIONS = """
ENGINE *ENGINE_get_first(void);
ENGINE *ENGINE_get_last(void);
ENGINE *ENGINE_get_next(ENGINE *);
ENGINE *ENGINE_get_prev(ENGINE *);
int ENGINE_add(ENGINE *);
int ENGINE_remove(ENGINE *);
ENGINE *ENGINE_by_id(const char *);
int ENGINE_init(ENGINE *);
int ENGINE_finish(ENGINE *);
int ENGINE_free(ENGINE *);
void ENGINE_cleanup(void);
void ENGINE_load_dynamic(void);
void ENGINE_load_builtin_engines(void);
int ENGINE_ctrl_cmd_string(ENGINE *, const char *, const char *, int);
int ENGINE_set_default(ENGINE *, unsigned int);
int ENGINE_register_complete(ENGINE *);

int ENGINE_set_default_RSA(ENGINE *);
int ENGINE_set_default_string(ENGINE *, const char *);
int ENGINE_set_default_DSA(ENGINE *);
int ENGINE_set_default_ECDH(ENGINE *);
int ENGINE_set_default_ECDSA(ENGINE *);
int ENGINE_set_default_DH(ENGINE *);
int ENGINE_set_default_RAND(ENGINE *);
int ENGINE_set_default_ciphers(ENGINE *);
int ENGINE_set_default_digests(ENGINE *);
"""

MACROS = """
#define ENGINE_METHOD_RSA ...
#define ENGINE_METHOD_DSA ...
#define ENGINE_METHOD_RAND ...
#define ENGINE_METHOD_ECDH ...
#define ENGINE_METHOD_ECDSA ...
#define ENGINE_METHOD_CIPHERS ...
#define ENGINE_METHOD_DIGESTS ...
#define ENGINE_METHOD_STORE ...
#define ENGINE_METHOD_ALL ...
#define ENGINE_METHOD_NONE ...
"""

CUSTOMIZATIONS = """
"""

CONDITIONAL_NAMES = {}
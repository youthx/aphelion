# opengl/constants.py

# --- Clear buffer bits ---
GL_COLOR_BUFFER_BIT                  = 0x00004000
GL_DEPTH_BUFFER_BIT                  = 0x00000100
GL_STENCIL_BUFFER_BIT                = 0x00000400

# --- Boolean ---
GL_FALSE                           = 0
GL_TRUE                            = 1

# --- Data types ---
GL_BYTE                            = 0x1400
GL_UNSIGNED_BYTE                   = 0x1401
GL_SHORT                           = 0x1402
GL_UNSIGNED_SHORT                  = 0x1403
GL_INT                             = 0x1404
GL_UNSIGNED_INT                    = 0x1405
GL_FLOAT                           = 0x1406
GL_DOUBLE                          = 0x140A
GL_HALF_FLOAT                     = 0x140B
GL_FIXED                           = 0x140C
GL_INT_2_10_10_10_REV             = 0x8D9F

# --- Primitive types ---
GL_POINTS                         = 0x0000
GL_LINES                          = 0x0001
GL_LINE_LOOP                     = 0x0002
GL_LINE_STRIP                    = 0x0003
GL_TRIANGLES                     = 0x0004
GL_TRIANGLE_STRIP                = 0x0005
GL_TRIANGLE_FAN                  = 0x0006
GL_LINES_ADJACENCY               = 0x000A
GL_LINE_STRIP_ADJACENCY          = 0x000B
GL_TRIANGLES_ADJACENCY           = 0x000C
GL_TRIANGLE_STRIP_ADJACENCY      = 0x000D
GL_PATCHES                      = 0x000E

# --- Buffer targets ---
GL_ARRAY_BUFFER                  = 0x8892
GL_ELEMENT_ARRAY_BUFFER          = 0x8893
GL_PIXEL_PACK_BUFFER             = 0x88EB
GL_PIXEL_UNPACK_BUFFER           = 0x88EC
GL_UNIFORM_BUFFER                = 0x8A11
GL_TEXTURE_BUFFER                = 0x8C2A
GL_TRANSFORM_FEEDBACK_BUFFER     = 0x8C8E
GL_COPY_READ_BUFFER              = 0x8F36
GL_COPY_WRITE_BUFFER             = 0x8F37
GL_DRAW_INDIRECT_BUFFER          = 0x8F3F
GL_ATOMIC_COUNTER_BUFFER         = 0x92C0
GL_DISPATCH_INDIRECT_BUFFER      = 0x90EE
GL_SHADER_STORAGE_BUFFER         = 0x90D2

# --- Buffer usage hints ---
GL_STREAM_DRAW                  = 0x88E0
GL_STREAM_READ                  = 0x88E1
GL_STREAM_COPY                  = 0x88E2
GL_STATIC_DRAW                  = 0x88E4
GL_STATIC_READ                  = 0x88E5
GL_STATIC_COPY                  = 0x88E6
GL_DYNAMIC_DRAW                 = 0x88E8
GL_DYNAMIC_READ                 = 0x88E9
GL_DYNAMIC_COPY                 = 0x88EA

# --- Shader types ---
GL_VERTEX_SHADER                = 0x8B31
GL_FRAGMENT_SHADER              = 0x8B30
GL_GEOMETRY_SHADER             = 0x8DD9
GL_TESS_CONTROL_SHADER         = 0x8E88
GL_TESS_EVALUATION_SHADER      = 0x8E87
GL_COMPUTE_SHADER              = 0x91B9

# --- Shader parameter names ---
GL_COMPILE_STATUS              = 0x8B81
GL_INFO_LOG_LENGTH             = 0x8B84
GL_SHADER_SOURCE_LENGTH        = 0x8B88
GL_SHADER_COMPILER             = 0x8DFA
GL_SHADER_BINARY_FORMATS       = 0x8DF8
GL_NUM_SHADER_BINARY_FORMATS   = 0x8DF9

# --- Program parameter names ---
GL_LINK_STATUS                = 0x8B82
GL_VALIDATE_STATUS            = 0x8B83
GL_ACTIVE_UNIFORMS            = 0x8B86
GL_ACTIVE_UNIFORM_MAX_LENGTH  = 0x8B87
GL_ACTIVE_ATTRIBUTES          = 0x8B89
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH= 0x8B8A
GL_PROGRAM_BINARY_RETRIEVABLE_HINT = 0x8257
GL_PROGRAM_BINARY_LENGTH       = 0x8741
GL_PROGRAM_SEPARABLE           = 0x8258

# --- Program pipeline parameters ---
GL_PROGRAM_PIPELINE_BINDING  = 0x825A

# --- Uniform types ---
GL_FLOAT_VEC2                = 0x8B50
GL_FLOAT_VEC3                = 0x8B51
GL_FLOAT_VEC4                = 0x8B52
GL_INT_VEC2                  = 0x8B53
GL_INT_VEC3                  = 0x8B54
GL_INT_VEC4                  = 0x8B55
GL_BOOL                      = 0x8B56
GL_BOOL_VEC2                 = 0x8B57
GL_BOOL_VEC3                 = 0x8B58
GL_BOOL_VEC4                 = 0x8B59
GL_FLOAT_MAT2                = 0x8B5A
GL_FLOAT_MAT3                = 0x8B5B
GL_FLOAT_MAT4                = 0x8B5C
GL_FLOAT_MAT2x3              = 0x8B65
GL_FLOAT_MAT2x4              = 0x8B66
GL_FLOAT_MAT3x2              = 0x8B67
GL_FLOAT_MAT3x4              = 0x8B68
GL_FLOAT_MAT4x2              = 0x8B69
GL_FLOAT_MAT4x3              = 0x8B6A
GL_SAMPLER_1D                = 0x8B5D
GL_SAMPLER_2D                = 0x8B5E
GL_SAMPLER_3D                = 0x8B5F
GL_SAMPLER_CUBE              = 0x8B60
GL_SAMPLER_1D_SHADOW         = 0x8B61
GL_SAMPLER_2D_SHADOW         = 0x8B62
GL_SAMPLER_1D_ARRAY          = 0x8DC0
GL_SAMPLER_2D_ARRAY          = 0x8DC1
GL_SAMPLER_1D_ARRAY_SHADOW   = 0x8DC3
GL_SAMPLER_2D_ARRAY_SHADOW   = 0x8DC4
GL_SAMPLER_CUBE_SHADOW       = 0x8DC5
GL_SAMPLER_BUFFER            = 0x8DC2
GL_SAMPLER_2D_MULTISAMPLE    = 0x9108
GL_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910B
GL_INT_SAMPLER_1D            = 0x8DC9
GL_INT_SAMPLER_2D            = 0x8DCA
GL_INT_SAMPLER_3D            = 0x8DCB
GL_INT_SAMPLER_CUBE          = 0x8DCC
GL_INT_SAMPLER_1D_ARRAY      = 0x8DCF
GL_INT_SAMPLER_2D_ARRAY      = 0x8DD0
GL_INT_SAMPLER_2D_MULTISAMPLE= 0x9109
GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910C
GL_UNSIGNED_INT_SAMPLER_1D   = 0x8DD1
GL_UNSIGNED_INT_SAMPLER_2D   = 0x8DD2
GL_UNSIGNED_INT_SAMPLER_3D   = 0x8DD3
GL_UNSIGNED_INT_SAMPLER_CUBE = 0x8DD4
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY = 0x8DD6
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x8DD7
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 0x910A
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910D

# --- Texture targets ---
GL_TEXTURE_1D                 = 0x0DE0
GL_TEXTURE_2D                 = 0x0DE1
GL_TEXTURE_3D                 = 0x806F
GL_TEXTURE_1D_ARRAY           = 0x8C18
GL_TEXTURE_2D_ARRAY           = 0x8C1A
GL_TEXTURE_RECTANGLE          = 0x84F5
GL_TEXTURE_CUBE_MAP           = 0x8513
GL_TEXTURE_CUBE_MAP_POSITIVE_X= 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X= 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y= 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y= 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z= 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z= 0x851A
GL_TEXTURE_BUFFER             = 0x8C2A
GL_TEXTURE_2D_MULTISAMPLE     = 0x9100
GL_TEXTURE_2D_MULTISAMPLE_ARRAY= 0x9102

# --- Texture parameters ---
GL_TEXTURE_MAG_FILTER          = 0x2800
GL_TEXTURE_MIN_FILTER          = 0x2801
GL_TEXTURE_WRAP_S              = 0x2802
GL_TEXTURE_WRAP_T              = 0x2803
GL_TEXTURE_WRAP_R              = 0x8072
GL_TEXTURE_BASE_LEVEL          = 0x813C
GL_TEXTURE_MAX_LEVEL           = 0x813D
GL_TEXTURE_MAX_LOD             = 0x813B
GL_TEXTURE_LOD_BIAS            = 0x8501
GL_TEXTURE_COMPARE_MODE        = 0x884C
GL_TEXTURE_COMPARE_FUNC        = 0x884D
GL_DEPTH_TEXTURE_MODE          = 0x884B

# --- Texture wrap modes ---
GL_REPEAT                     = 0x2901
GL_MIRRORED_REPEAT            = 0x8370
GL_CLAMP_TO_EDGE              = 0x812F
GL_CLAMP_TO_BORDER            = 0x812D

# --- Texture filters ---
GL_NEAREST                    = 0x2600
GL_LINEAR                     = 0x2601
GL_NEAREST_MIPMAP_NEAREST    = 0x2700
GL_LINEAR_MIPMAP_NEAREST     = 0x2701
GL_NEAREST_MIPMAP_LINEAR     = 0x2702
GL_LINEAR_MIPMAP_LINEAR      = 0x2703

# --- Framebuffer targets ---
GL_FRAMEBUFFER                = 0x8D40
GL_DRAW_FRAMEBUFFER           = 0x8CA9
GL_READ_FRAMEBUFFER           = 0x8CA8

# --- Framebuffer attachment points ---
GL_COLOR_ATTACHMENT0          = 0x8CE0
GL_COLOR_ATTACHMENT1          = 0x8CE1
GL_COLOR_ATTACHMENT2          = 0x8CE2
GL_COLOR_ATTACHMENT3          = 0x8CE3
GL_DEPTH_ATTACHMENT           = 0x8D00
GL_STENCIL_ATTACHMENT         = 0x8D20
GL_DEPTH_STENCIL_ATTACHMENT   = 0x821A

# --- Framebuffer status ---
GL_FRAMEBUFFER_COMPLETE                         = 0x8CD5
GL_FRAMEBUFFER_UNDEFINED                        = 0x8219
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT            = 0x8CD6
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT    = 0x8CD7
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER           = 0x8CDB
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER           = 0x8CDC
GL_FRAMEBUFFER_UNSUPPORTED                       = 0x8CDD
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE            = 0x8D56
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS          = 0x8DA8

# --- Vertex Array Objects ---
GL_VERTEX_ARRAY                = 0x8074

# --- Capability bits for glEnable/glDisable ---
GL_DEPTH_TEST                 = 0x0B71
GL_STENCIL_TEST               = 0x0B90
GL_BLEND                      = 0x0BE2
GL_CULL_FACE                  = 0x0B44
GL_SCISSOR_TEST               = 0x0C11
GL_POLYGON_OFFSET_FILL        = 0x8037
GL_SAMPLE_ALPHA_TO_COVERAGE   = 0x809E
GL_SAMPLE_COVERAGE            = 0x80A0
GL_MULTISAMPLE                = 0x809D
GL_SAMPLE_MASK                = 0x8E51

# --- Blending factors ---
GL_ZERO                      = 0
GL_ONE                       = 1
GL_SRC_COLOR                 = 0x0300
GL_ONE_MINUS_SRC_COLOR       = 0x0301
GL_DST_COLOR                 = 0x0306
GL_ONE_MINUS_DST_COLOR       = 0x0307
GL_SRC_ALPHA                 = 0x0302
GL_ONE_MINUS_SRC_ALPHA       = 0x0303
GL_DST_ALPHA                 = 0x0304
GL_ONE_MINUS_DST_ALPHA       = 0x0305
GL_CONSTANT_COLOR            = 0x8001
GL_ONE_MINUS_CONSTANT_COLOR  = 0x8002
GL_CONSTANT_ALPHA            = 0x8003
GL_ONE_MINUS_CONSTANT_ALPHA  = 0x8004
GL_SRC_ALPHA_SATURATE        = 0x0308

# --- Error codes ---
GL_NO_ERROR                  = 0
GL_INVALID_ENUM              = 0x0500
GL_INVALID_VALUE             = 0x0501
GL_INVALID_OPERATION         = 0x0502
GL_STACK_OVERFLOW            = 0x0503
GL_STACK_UNDERFLOW           = 0x0504
GL_OUT_OF_MEMORY             = 0x0505
GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506

# --- Polygon modes ---
GL_POINT                    = 0x1B00
GL_LINE                     = 0x1B01
GL_FILL                     = 0x1B02

# --- Stencil functions ---
GL_NEVER                    = 0x0200
GL_LESS                     = 0x0201
GL_EQUAL                    = 0x0202
GL_LEQUAL                   = 0x0203
GL_GREATER                  = 0x0204
GL_NOTEQUAL                 = 0x0205
GL_GEQUAL                   = 0x0206
GL_ALWAYS                   = 0x0207

# --- Stencil operations ---
GL_KEEP                     = 0x1E00
GL_REPLACE                  = 0x1E01
GL_INCR                     = 0x1E02
GL_INCR_WRAP                = 0x8507
GL_DECR                     = 0x1E03
GL_DECR_WRAP                = 0x8508
GL_INVERT                   = 0x150A

# --- Pixel formats ---
GL_RGB                      = 0x1907
GL_RGBA                     = 0x1908
GL_LUMINANCE                = 0x1909
GL_LUMINANCE_ALPHA          = 0x190A
GL_DEPTH_COMPONENT          = 0x1902
GL_DEPTH_STENCIL            = 0x84F9
GL_RED                      = 0x1903
GL_RG                       = 0x8227

# --- Front face winding ---
GL_CW                       = 0x0900
GL_CCW                      = 0x0901

# --- Hints ---
GL_DONT_CARE                = 0x1100
GL_FASTEST                  = 0x1101
GL_NICEST                   = 0x1102

# --- Sync ---
GL_SYNC_GPU_COMMANDS_COMPLETE = 0x9117
GL_ALREADY_SIGNALED         = 0x911A
GL_TIMEOUT_EXPIRED          = 0x911B
GL_CONDITION_SATISFIED      = 0x911C
GL_WAIT_FAILED              = 0x911D

# --- Query targets ---
GL_SAMPLES_PASSED           = 0x8914
GL_ANY_SAMPLES_PASSED       = 0x8C2F
GL_PRIMITIVES_GENERATED     = 0x8C87
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 0x8C88

# --- Sync objects ---
GL_SYNC_FENCE               = 0x9116

# --- Additional ---
GL_MAJOR_VERSION            = 0x821B
GL_MINOR_VERSION            = 0x821C
GL_NUM_EXTENSIONS           = 0x821D

GL_CONTEXT_FLAGS            = 0x821E
GL_CONTEXT_PROFILE_MASK     = 0x9126
GL_CONTEXT_CORE_PROFILE_BIT = 0x00000001
GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 0x00000002

# --- Debug output ---
GL_DEBUG_OUTPUT             = 0x92E0
GL_DEBUG_OUTPUT_SYNCHRONOUS = 0x8242
GL_DEBUG_SEVERITY_HIGH      = 0x9146
GL_DEBUG_SEVERITY_MEDIUM    = 0x9147
GL_DEBUG_SEVERITY_LOW       = 0x9148
GL_DEBUG_SEVERITY_NOTIFICATION = 0x826B

# --- Buffer storage flags (ARB) ---
GL_MAP_READ_BIT             = 0x0001
GL_MAP_WRITE_BIT            = 0x0002
GL_MAP_INVALIDATE_RANGE_BIT = 0x0004
GL_MAP_INVALIDATE_BUFFER_BIT= 0x0008
GL_MAP_FLUSH_EXPLICIT_BIT   = 0x0010
GL_MAP_UNSYNCHRONIZED_BIT   = 0x0020

# --- Texture swizzle ---
GL_TEXTURE_SWIZZLE_R        = 0x8E42
GL_TEXTURE_SWIZZLE_G        = 0x8E43
GL_TEXTURE_SWIZZLE_B        = 0x8E44
GL_TEXTURE_SWIZZLE_A        = 0x8E45

# --- Geometry shader input/output types ---
GL_POINTS                    = 0x0000
GL_LINES                     = 0x0001
GL_LINES_ADJACENCY           = 0x000A
GL_TRIANGLES                 = 0x0004
GL_TRIANGLES_ADJACENCY       = 0x000C
GL_PATCHES                   = 0x000E

# --- Additional texture formats ---
GL_COMPRESSED_RGB_S3TC_DXT1_EXT = 0x83F0
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT= 0x83F1
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT= 0x83F2
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT= 0x83F3

# (Add more extensions and enums as you need)


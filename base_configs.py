NUM_CHANNELS = 2

convup_no_dtw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###IdentityScalarTimewarper###
     scalar_timewarper_name = "identity_scalar_timewarper",
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     encoder_name="convolutional_encoder",
     emb_conv_layers_channels = [16,16],#[],#
     emb_conv_layers_strides = [2,2],#[],#
     emb_conv_layers_kernel_sizes = [3,3],#[],#
     emb_fc_layers_num_features = [16],#[],#
     ###########################
     #########Decoding##########
     ###########################
     ###OneDConvDecoder###
     decoder_name="convolutional_decoder_upsampling",
     ### Complicated enough model
     dec_gen_fc_layers_num_features = [25*NUM_CHANNELS*16],
     dec_gen_first_traj_len=25,
     dec_gen_conv_layers_channels = [NUM_CHANNELS*10,NUM_CHANNELS*10,NUM_CHANNELS],
     dec_gen_upsampling_factors = [2,2,2],
     dec_gen_conv_layers_kernel_sizes = [3,3,3],
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###IdentityTimewarper### 
     vector_timewarper_name="identity_vector_timewarper"
     )

conv_no_dtw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###IdentityScalarTimewarper###
     scalar_timewarper_name = "identity_scalar_timewarper",
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     encoder_name="convolutional_encoder",
     emb_conv_layers_channels = [16,16],#[],#
     emb_conv_layers_strides = [2,2],#[],#
     emb_conv_layers_kernel_sizes = [3,3],#[],#
     emb_fc_layers_num_features = [16],#[],#
     ###########################
     #########Decoding##########
     ###########################
     ###OneDConvDecoder###
     decoder_name="convolutional_decoder",
     ### Complicated enough model
     dec_gen_fc_layers_num_features = [100*NUM_CHANNELS,30*NUM_CHANNELS*10],
     dec_gen_first_traj_len=30,
     dec_gen_conv_layers_channels = [NUM_CHANNELS*10,NUM_CHANNELS*10,NUM_CHANNELS],
     dec_gen_conv_layers_strides = [2,2,2],
     dec_gen_conv_layers_kernel_sizes = [3,3,3],
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###IdentityTimewarper### 
     vector_timewarper_name="identity_vector_timewarper"
     )

conv_dtw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###IdentityScalarTimewarper###
     scalar_timewarper_name = "identity_scalar_timewarper",
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     encoder_name="convolutional_encoder",
     emb_conv_layers_channels = [16,16],#[],#
     emb_conv_layers_strides = [2,2],#[],#
     emb_conv_layers_kernel_sizes = [3,3],#[],#
     emb_fc_layers_num_features = [16],#[],#
     ###########################
     #########Decoding##########
     ###########################
     ###OneDConvDecoder###
     decoder_name="convolutional_decoder",
     ### Complicated enough model
     dec_gen_fc_layers_num_features = [100*NUM_CHANNELS,30*NUM_CHANNELS*10],
     dec_gen_first_traj_len=30,
     dec_gen_conv_layers_channels = [NUM_CHANNELS*10,NUM_CHANNELS*10,NUM_CHANNELS],
     dec_gen_conv_layers_strides = [2,2,2],
     dec_gen_conv_layers_kernel_sizes = [3,3,3],
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###DTWTimewarper### 
     vector_timewarper_name="dtw_vector_timewarper",
     vector_timewarper_warps_recon_and_actual=True
     )

func_no_tw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###IdentityScalarTimewarper###
     scalar_timewarper_name = "identity_scalar_timewarper",
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     encoder_name="convolutional_encoder",
     emb_conv_layers_channels = [16,16],#[],#
     emb_conv_layers_strides = [2,2],#[],#
     emb_conv_layers_kernel_sizes = [3,3],#[],#
     emb_fc_layers_num_features = [16],#[],#
     ###########################
     #########Decoding##########
     ###########################
     ###FunctionStyleDecoder###
     decoder_name="functional_decoder",
     dec_template_motion_hidden_layers=[500,500],
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###IdentityTimewarper### 
     vector_timewarper_name="identity_vector_timewarper"
     )

func_tw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###ModeledParameterScalarTimewarper###
     scalar_timewarper_name = "modeled_scalar_timewarper",
     ## TimeWarpingRelated
     scaltw_granularity = 20,
     scaltw_emb_conv_layers_channels = [16,16],
     scaltw_emb_conv_layers_strides = [2,2],
     scaltw_emb_conv_layers_kernel_sizes = [3,3],
     scaltw_emb_fc_layers_num_features = [32],
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     encoder_name="convolutional_encoder",
     emb_conv_layers_channels = [16,16],#[],#
     emb_conv_layers_strides = [2,2],#[],#
     emb_conv_layers_kernel_sizes = [3,3],#[],#
     emb_fc_layers_num_features = [16],#[],#
     ###########################
     #########Decoding##########
     ###########################
     ###FunctionStyleDecoder###
     decoder_name="functional_decoder",
     dec_template_motion_hidden_layers=[500,500],
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###IdentityTimewarper### 
     vector_timewarper_name="identity_vector_timewarper"
     )

trans_func_tw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###ModeledParameterScalarTimewarper###
     scalar_timewarper_name = "modeled_scalar_timewarper",
     ## TimeWarpingRelated
     scaltw_granularity = 20,
     scaltw_emb_conv_layers_channels = [16,16],
     scaltw_emb_conv_layers_strides = [2,2],
     scaltw_emb_conv_layers_kernel_sizes = [3,3],
     scaltw_emb_fc_layers_num_features = [32],
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     encoder_name="transformer_encoder",
     enc_attention_dims_per_head = 4,
     enc_append_time_dim = True,
     ###########################
     #########Decoding##########
     ###########################
     ###FunctionStyleDecoder###
     decoder_name="functional_decoder",
     dec_template_motion_hidden_layers=[500,500],
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###IdentityTimewarper### 
     vector_timewarper_name="identity_vector_timewarper"
     )

func_side_no_tw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###IdentityScalarTimewarper###
     scalar_timewarper_name = "identity_scalar_timewarper",
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     encoder_name="convolutional_encoder",
     emb_conv_layers_channels = [16,16],#[],#
     emb_conv_layers_strides = [2,2],#[],#
     emb_conv_layers_kernel_sizes = [3,3],#[],#
     emb_fc_layers_num_features = [16],#[],#
     ###########################
     #########Decoding##########
     ###########################
     ###FunctionStyleDecoder###
     decoder_name="functional_decoder_complicated",
     dec_template_motion_hidden_layers=[500,500],
     dec_complicated_function_hidden_dims = [16],
     dec_complicated_function_latent_size = 16,
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###IdentityTimewarper### 
     vector_timewarper_name="identity_vector_timewarper"
     )

func_side_tw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###ModeledParameterScalarTimewarper###
     scalar_timewarper_name = "modeled_scalar_timewarper",
     ## TimeWarpingRelated
     scaltw_granularity = 20,
     scaltw_emb_conv_layers_channels = [16,16],
     scaltw_emb_conv_layers_strides = [2,2],
     scaltw_emb_conv_layers_kernel_sizes = [3,3],
     scaltw_emb_fc_layers_num_features = [32],
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     encoder_name="convolutional_encoder",
     emb_conv_layers_channels = [32,64,32],#[],#
     emb_conv_layers_strides = [2,2,1],#[],#
     emb_conv_layers_kernel_sizes = [3,3,3],#[],#
     emb_fc_layers_num_features = [128],#[],#
     ###########################
     #########Decoding##########
     ###########################
     ###FunctionStyleDecoder###
     decoder_name="functional_decoder_complicated",
     dec_template_motion_hidden_layers=[500,500],
     dec_complicated_function_hidden_dims = [16],
     dec_complicated_function_latent_size = 16,
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###IdentityTimewarper### 
     vector_timewarper_name="identity_vector_timewarper"
     )

self_attn_tw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###ModeledParameterScalarTimewarper###
     scalar_timewarper_name = "modeled_scalar_timewarper",
     ## TimeWarpingRelated
     scaltw_granularity = 20,
     scaltw_emb_conv_layers_channels = [16,16],
     scaltw_emb_conv_layers_strides = [2,2],
     scaltw_emb_conv_layers_kernel_sizes = [3,3],
     scaltw_emb_fc_layers_num_features = [32],
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     #encoder_name="convolutional_encoder",
     #emb_conv_layers_channels = [32,64,32],#[],#
     #emb_conv_layers_strides = [2,2,1],#[],#
     #emb_conv_layers_kernel_sizes = [3,3,3],#[],#
     #emb_fc_layers_num_features = [128],#[],#
     ###SelfAttention###
     encoder_name="self_attention_transformer_encoder",
     emb_nonlinearity="ELU",
     enc_attention_dims_per_head = 128,
     enc_attention_num_heads = 16,
     enc_append_time_dim = True,
     ###########################
     #########Decoding##########
     ###########################
     ###FunctionStyleDecoder###
     decoder_name="functional_decoder_complicated",
     dec_template_motion_hidden_layers=[500,500],
     dec_complicated_function_hidden_dims = [16],
     dec_complicated_function_latent_size = 16,
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###IdentityTimewarper### 
     vector_timewarper_name="identity_vector_timewarper"
     )

self_attn_no_tw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###ModeledParameterScalarTimewarper###
     scalar_timewarper_name = "identity_scalar_timewarper",
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     #encoder_name="convolutional_encoder",
     #emb_conv_layers_channels = [32,64,32],#[],#
     #emb_conv_layers_strides = [2,2,1],#[],#
     #emb_conv_layers_kernel_sizes = [3,3,3],#[],#
     #emb_fc_layers_num_features = [128],#[],#
     ###SelfAttention###
     encoder_name="self_attention_transformer_encoder",
     emb_nonlinearity="ReLU",
     enc_attention_dims_per_head = 128,
     enc_attention_num_heads = 16,
     enc_append_time_dim = True,
     ###########################
     #########Decoding##########
     ###########################
     ###FunctionStyleDecoder###
     decoder_name="functional_decoder_complicated",
     dec_template_motion_hidden_layers=[500,500],
     dec_complicated_function_hidden_dims = [16],
     dec_complicated_function_latent_size = 16,
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###IdentityTimewarper### 
     vector_timewarper_name="identity_vector_timewarper"
     )

self_attn_tw = dict(
     ###########################
     #####ScalarTimeWarping#####
     ###########################
     ###ModeledParameterScalarTimewarper###
     scalar_timewarper_name = "modeled_scalar_timewarper",
     ## TimeWarpingRelated
     scaltw_granularity = 20,
     scaltw_emb_conv_layers_channels = [16,16],
     scaltw_emb_conv_layers_strides = [2,2],
     scaltw_emb_conv_layers_kernel_sizes = [3,3],
     scaltw_emb_fc_layers_num_features = [32],
     ###########################
     #########Encoding##########
     ###########################
     ###OneDConvEncoder###
     #encoder_name="convolutional_encoder",
     #emb_conv_layers_channels = [32,64,32],#[],#
     #emb_conv_layers_strides = [2,2,1],#[],#
     #emb_conv_layers_kernel_sizes = [3,3,3],#[],#
     #emb_fc_layers_num_features = [128],#[],#
     ###SelfAttention###
     encoder_name="self_attention_transformer_encoder",
     emb_nonlinearity="ELU",
     enc_attention_dims_per_head = 128,
     enc_attention_num_heads = 16,
     enc_append_time_dim = True,
     ###########################
     #########Decoding##########
     ###########################
     ###FunctionStyleDecoder###
     decoder_name="functional_decoder_complicated",
     dec_template_motion_hidden_layers=[500,500],
     dec_complicated_function_hidden_dims = [16],
     dec_complicated_function_latent_size = 16,
     ###########################
     #####VectorTimewarping#####
     ###########################
     ###IdentityTimewarper### 
     vector_timewarper_name="identity_vector_timewarper"
     )
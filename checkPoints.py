### if I want to start to initialize from 0 step
save_dir = "chckPts/"
save_prefix = "save"

start_step = 0
load_path = None
# load_path = save_dir + save_prefix + str(start_step) + ".ckpt"


sess = tf.Session()
saver = tf.train.Saver()
    
ckpt = tf.train.get_checkpoint_state(save_dir)
if load_path is not None and ckpt and ckpt.model_checkpoint_path:
    try:
        saver.restore(sess, load_path)
        print("LOADED CHECKPOINT")
    except:
        print("FAILED TO LOAD CHECKPOINT")
        exit()
else:
    init = tf.initialize_all_variables()
    sess.run(init)
    
### if I want to start to initialize from 5000 step
save_dir = "chckPts/"
save_prefix = "save"

start_step = 5000
# load_path = None
load_path = save_dir + save_prefix + str(start_step) + ".ckpt"


sess = tf.Session()
saver = tf.train.Saver()
    
ckpt = tf.train.get_checkpoint_state(save_dir)
if load_path is not None and ckpt and ckpt.model_checkpoint_path:
    try:
        saver.restore(sess, load_path)
        print("LOADED CHECKPOINT")
    except:
        print("FAILED TO LOAD CHECKPOINT")
        exit()
else:
    init = tf.initialize_all_variables()
    sess.run(init)

import importlib.metadata as impmeta

#=========================================================================================
# Truenet help, description and epilog messages to display
# Vaanathi Sundaresan
# 09-03-2021, Oxford
#=========================================================================================

def help_descs():
    version = impmeta.version('truenet')
    helps = {
        'mainparser' :
        "truenet: Triplanar ensemble U-Net model, v" + str(version) + "\n"
        "   \n"
        "Sub-commands available:\n"
        "       truenet train           Training a TrUE-Net model from scratch\n"
        "       truenet evaluate        Applying a saved/pretrained TrUE-Net model for testing\n"
        "       truenet fine_tune       Fine-tuning a saved/pretrained TrUE-Net model\n"
        "       truenet cross_validate  Cross-validation of TrUE-Net model\n"
        "   \n"
        "   \n"
        "For detailed help regarding the options for each command,\n"
        "type truenet <command> --help (e.g. truenet train --help)\n"
        "   \n",

        'train':
        '   \n'
        'truenet train: training the TrUE-Net model from scratch, v' + str(version) + '\n'
        '   \n'
        'Usage: truenet train -i <input_directory> -m <model_directory> [options]\n'
        '   \n'
        'Compulsory arguments:\n'
        '       -i, --inp_dir                       Directory containing FLAIR and T1 images for training\n'
        '       -l, --label_dir                     Directory containing lesion manual masks\n'
        '       -m, --model_dir                     Directory where the training model or weights need to be saved\n'
        '   \n'
        'Optional arguments:\n'
        '       -tr_prop, --train_prop              Proportion of data used for training [0, 1]. The rest will be used for validation [default = 0.8]\n'
        '       -bfactor, --batch_factor            Number of subjects to be considered for each mini-epoch [default = 10]\n'
        '       -loss, --loss_function              Applying spatial weights to loss function. Options: weighted, nweighted [default=weighted]\n'
        '       -gdir, --gmdist_dir                 Directory containing GM distance map images. Required if -loss=weighted [default = None]\n'
        '       -vdir, --ventdist_dir               Directory containing ventricle distance map images. Required if -loss=weighted [default = None]\n'
        '       -nclass, --num_classes              Number of classes to consider in the target labels (nclass=2 will consider only 0 and 1 in labels;\n'
        '                                           any additional class will be considered part of background class [default = 2]\n'
        '       -plane, --acq_plane                 The plane in which the model needs to be trained. Options: axial, sagittal, coronal, all [default = all]\n'
        '       -ilr, --init_learng_rate            Initial LR to use in scheduler [0, 0.1] [default=0.001]\n'
        '       -lrm, --lr_sch_mlstone              Milestones for LR scheduler (e.g. -lrm 5 10 - to reduce LR at 5th and 10th epochs) [default = 10]\n'
        '       -gamma, --lr_sch_gamma              Factor by which the LR needs to be reduced in the LR scheduler [default = 0.1]\n'
        '       -opt, --optimizer                   Optimizer used for training. Options:adam, sgd [default = adam]\n'
        '       -bs, --batch_size                   Batch size used for training [default = 8]\n'
        '       -ep, --num_epochs                   Number of epochs for training [default = 60]\n'
        '       -eps, --epsilon                     Epsilon for adam optimiser (default=1e-4)\n'
        '       -mom, --momentum                    Momentum for sgd optimiser (default=0.9)\n'
        '       -es, --early_stop_val               Number of epochs to wait for progress (early stopping) [default = 20]\n'
        '       -sv_mod, --save_full_model          Saving the whole model instead of weights alone [default = False]\n'
        '       -sv_resume, --save_resume_training  Whether to save and resume training in case of interruptions (default-False)\n'
        '       -cp_type, --cp_save_type            Checkpoint to be saved. Options: best, last, everyN [default = last]\n'
        '       -cp_n, --cp_everyn_N                If -cv_type=everyN, the N value [default = 10]\n'
        '       -da, --data_augmentation            Applying data augmentation [default = True]\n'
        '       -af, --aug_factor                   Data inflation factor for augmentation [default = 2]\n'
        '       -v, --verbose                       Display debug messages [default = False]\n'
        '   \n',

        'evaluate':
        'truenet evaluate: testing the TrUE-Net model, v' + str(version) + '\n'
        '   \n'
        'Usage: truenet evaluate -i <input_directory> -m <model_directory> -o <output_directory> [options]'
        '   \n'
        'Compulsory arguments:\n'
        '       -i, --inp_dir                         Directory containing FLAIR and T1 images for testing\n'
        '       -m, --model_dir                       Model basename with absolute path. If you want to use pretrained model, use mwsc/ukbb\n'
        '       -o, --output_dir                      Directory for saving output predictions\n'
        '   \n'
        'Optional arguments:\n'
        '       -cpu, --use_cpu                       Force the model to evaluate the model on CPU (default=False)\n'
        '       -nclass, --num_classes                Number of classes in the labels used for training the model (for both pretrained models, -nclass=2) [default = 2]\n'
        '       -int, --intermediate                  Saving intermediate prediction results (individual planes) for each subject [default = False]\n'
        '       -cp_type, --cp_load_type              Checkpoint to be loaded. Options: best, last, everyN [default = last]\n'
        '       -cp_n, --cp_everyn_N                  If -cv_type = everyN, the N value [default = 10]\n'
        '       -v, --verbose                         Display debug messages [default = False]\n'
        '   \n',

    'fine_tune':
        'truenet fine_tune: training the TrUE-Net model from scratch, v' + str(version) + '\n'
        '   \n'
        'Usage: truenet fine_tune -i <input_directory> -m <model_directory> -o <output_directory> [options]\n'
        '   \n'
        '   \n'
        'Compulsory arguments:\n'
        '       -i, --inp_dir                         Path to the directory containing FLAIR and T1 images for fine-tuning\n'
        '       -l, --label_dir                       Directory containing lesion manual masks\n'
        '       -m, --model_dir                       Model basename with absolute path. If you want to use pretrained model, use mwsc/ukbb\n'
        '       -o, --output_dir                      Path to the directory where the fine-tuned model/weights need to be saved\n'
        '   \n'
        'Optional arguments:\n'
        '       -cpld_type, --cp_load_type            Checkpoint to be loaded. Options: best, last, everyN [default = last]\n'
        '       -cpld_n, --cpload_everyn_N            If everyN option was chosen for loading a checkpoint, the N value [default = 10]\n'
        '       -ftlayers, --ft_layers                Layers to fine-tune starting from the decoder (e.g. 1 2 -> final two two decoder layers)\n'
        '       -tr_prop, --train_prop                Proportion of data used for fine-tuning [0, 1]. The rest will be used for validation [default = 0.8]\n'
        '       -bfactor, --batch_factor              Number of subjects to be considered for each mini-epoch [default = 10]\n'
        '       -loss, --loss_function                Applying spatial weights to loss function. Options: weighted, nweighted [default=weighted]\n'
        '       -gdir, --gmdist_dir                   Directory containing GM distance map images. Required if -loss = weighted [default = None]\n'
        '       -vdir, --ventdist_dir                 Directory containing ventricle distance map images. Required if -loss = weighted [default = None]\n'
        '       -nclass, --num_classes                Number of classes to consider in the target labels (nclass=2 will consider only 0 and 1 in labels; \n'
        '                                             any additional class will be considered part of background class [default = 2]\n'
        '       -plane, --acq_plane                   The plane in which the model needs to be fine-tuned. Options: axial, sagittal, coronal, all [default = all]\n'
        '       -ilr, --init_learng_rate              Initial LR to use in scheduler for fine-tuning [0, 0.1] [default=0.0001]\n'
        '       -lrm, --lr_sch_mlstone                Milestones for LR scheduler (e.g. -lrm 5 10 - to reduce LR at 5th and 10th epochs) [default = 10]\n'
        '       -gamma, --lr_sch_gamma                Factor by which the LR needs to be reduced in the LR scheduler [default = 0.1]\n'
        '       -opt, --optimizer                     Optimizer used for fine-tuning. Options:adam, sgd [default = adam]\n'
        '       -eps, --epsilon                       Epsilon for adam optimiser (default=1e-4)\n'
        '       -mom, --momentum                      Momentum for sgd optimiser (default=0.9)\n'
        '       -sv_resume, --save_resume_training    Whether to save and resume training in case of interruptions (default-False)\n'
        '       -bs, --batch_size                     Batch size used for fine-tuning [default = 8]\n'
        '       -ep, --num_epochs                     Number of epochs for fine-tuning [default = 60]\n'
        '       -es, --early_stop_val                 Number of fine-tuning epochs to wait for progress (early stopping) [default = 20]\n'
        '       -sv_mod, --save_full_model            Saving the whole fine-tuned model instead of weights alone [default = False]\n'
        '       -cp_type, --cp_save_type              Checkpoint to be saved. Options: best, last, everyN [default = last]\n'
        '       -cp_n, --cp_everyn_N                  If -cv_type = everyN, the N value [default = 10]\n'
        '       -da, --data_augmentation              Applying data augmentation [default = True]\n'
        '       -af, --aug_factor                     Data inflation factor for augmentation [default = 2]\n'
        '       -v, --verbose                         Display debug messages [default = False]\n'
        '   \n',

    'cross_validate':
        'truenet cross_validate: cross-validation of the TrUE-Net model, v' + str(version) + '\n'
        '   \n'
        'Usage: truenet cross_validate -i <input_directory> -o <output_directory> [options]\n'
        '   \n'
        '   \n'
        'Compulsory arguments:\n'
        '       -i, --inp_dir                         Path to the directory containing FLAIR and T1 images for fine-tuning\n'
        '       -l, --label_dir                       Directory containing lesion manual masks\n'
        '       -o, --output_dir                      Path to the directory for saving output predictions\n'
        '   \n'
        'Optional arguments:\n'
        '       -tr_prop, --train_prop                Proportion of data used for training [0, 1]. The rest will be used for validation [default = 0.8]\n'
        '       -fold, --cv_fold                      Number of folds for cross-validation (default = 5)\n'
        '       -resume_fold, --resume_from_fold      Resume cross-validation from the specified fold (default = 1)\n'
        '       -bfactor, --batch_factor              Number of subjects to be considered for each mini-epoch [default = 10]\n'
        '       -loss, --loss_function                Applying spatial weights to loss function. Options: weighted, nweighted [default=weighted]\n'
        '       -gdir, --gmdist_dir                   Directory containing GM distance map images. Required if -loss = weighted [default = None]\n'
        '       -vdir, --ventdist_dir                 Directory containing ventricle distance map images. Required if -loss = weighted [default = None]\n'
        '       -nclass, --num_classes                Number of classes to consider in the target labels (nclass=2 will consider only 0 and 1 in labels; \n'
        '                                             any additional class will be considered part of background class [default = 2]\n'
        '       -plane, --acq_plane                   The plane in which the model needs to be trained. Options: axial, sagittal, coronal, all [default = all]\n'
        '       -ilr, --init_learng_rate              Initial LR to use in scheduler for training [0, 0.1] [default=0.0001]\n'
        '       -lrm, --lr_sch_mlstone                Milestones for LR scheduler (e.g. -lrm 5 10 - to reduce LR at 5th and 10th epochs) [default = 10]\n'
        '       -gamma, --lr_sch_gamma                Factor by which the LR needs to be reduced in the LR scheduler [default = 0.1]\n'
        '       -opt, --optimizer                     Optimizer used for training. Options:adam, sgd [default = adam]\n'
        '       -bs, --batch_size                     Batch size used for fine-tuning [default = 8]\n'
        '       -eps, --epsilon                       Epsilon for adam optimiser (default=1e-4)\n'
        '       -mom, --momentum                      Momentum for sgd optimiser (default=0.9)\n'
        '       -mom, --momentum                      Momentum for sgd optimiser (default=0.9)\n'
        '       -sv, --save_checkpoint                Whether to save any checkpoint (default=False)\n'
        '       -sv_resume, --save_resume_training    Whether to save and resume training in case of interruptions (default-False)\n'
        '       -cp_type, --cp_save_type              Checkpoint to be saved. Options: best, last, everyN [default = last]\n'
        '       -cp_n, --cp_everyn_N                  If -cv_type=everyN, the N value [default = 10]\n'
        '       -ep, --num_epochs                     Number of epochs for fine-tuning [default = 60]\n'
        '       -es, --early_stop_val                 Number of fine-tuning epochs to wait for progress (early stopping) [default = 20]\n'
        '       -int, --intermediate                  Saving intermediate prediction results (individual planes) for each subject [default = False]\n'
        '       -da, --data_augmentation              Applying data augmentation [default = True]\n'
        '       -af, --aug_factor                     Data inflation factor for augmentation [default = 2]\n'
        '       -v, --verbose                         Display debug messages [default = False]\n'
        '   \n'
    }

    return helps

def desc_descs():
    version = impmeta.version("truenet")
    descs = {
        'mainparser' :
        "truenet: Triplanar ensemble U-Net model, v" + str(version) + "\n"
        "   \n"
        "Sub-commands available:\n"
        "       truenet train           Training a TrUE-Net model from scratch\n"
        "       truenet evaluate        Applying a saved/pretrained TrUE-Net model for testing\n"
        "       truenet fine_tune       Fine-tuning a saved/pretrained TrUE-Net model \n"
        "       truenet cross_validate  Cross-validation of TrUE-Net model\n"
        "   \n",

        'train':
        '   \n'
        'truenet: Triplanar ensemble U-Net model, v' + str(version) + '\n'
        '   \n'
        'The \'train\' command trains the TrUE-Net model from scratch using the training subjects specified in\n'
        'the input directory. The FLAIR and T1 volumes should be named as \'<subj_name>_FLAIR.nii.gz\'\n'
        'and \'<subj_name>_T1.nii.gz\' respectively\n'
        '   \n',

        'evaluate':
        '   \n'
        'truenet: Triplanar ensemble U-Net model, v' + str(version) + '\n'
        '   \n'
        'The \'evaluate\' command is used for testing the TrUE-Net model on the test subjects specified in\n'
        'the input directory. The FLAIR and T1 volumes should be named as \'<subj_name>_FLAIR.nii.gz\' and\n'
        '\'<subj_name>_T1.nii.gz\'respectively\n'
        '   \n',

        'fine_tune':
        '   \n'
        'truenet: Triplanar ensemble U-Net model, v' + str(version) + '\n'
        '   \n'
        'The \'fine_tune\' command fine-tunes a pretrained TrUE-Net model (from a model directory) on the\n'
        'training subjects specified in the input directory. The FLAIR and T1 volumes should be named as\n'
        '\'<subj_name>_FLAIR.nii.gz\' and \'<subj_name>_T1.nii.gz\'respectively\n'
        '   \n',

        'cross_validate':
        '   \n'
        'truenet: Triplanar ensemble U-Net model, v' + str(version) + '\n'
        '   \n'
        'The \'cross_validate\' command performs cross-validation of the TrUE-Net model on the\n'
        'subjects specified in the input directory. The FLAIR and T1 volumes should be named as\n'
        '\'<subj_name>_FLAIR.nii.gz\' and \'<subj_name>_T1.nii.gz\'respectively\n'
        '   \n'
    }
    return descs

def epilog_descs():
    epilogs = {
        'mainparser' :
        "   \n"
        "For detailed help regarding the options for each command,\n"
        "type truenet <command> --help or -h (e.g. truenet train --help, truenet train -h)\n"
        "   \n",

        'subparsers' :
        '   \n'
        "For detailed help regarding the options for each argument,\n"
        "refer to the user-guide or readme document. For more details on\n"
        "TrUE-Net, refer to https://www.biorxiv.org/content/10.1101/2020.07.24.219485v1.full\n"
        "   \n",
    }
    return epilogs

(hytouch
  (dependencies
    '("jupyter==5.7.4"
    "pytorch==1.0.0"
    "numpy"
    "hy==0.1.5"))

  (tasks
    '(("lab" "jupyter lab")
     ("notebook" "jupyter notebook"))))

; implementation note: these style may require macros

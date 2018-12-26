(setv package {
  "dependencies"
  {"numpy" {}
   "hy==0.15.0" {}
   "jupyter" {}}

   "tasks"
   {"lab" ["jupyter" "lab"]
   "notebook" ["jupyter" "notebook"]
   "test" ["ls" "/home/takuma"]}})

require 'html/proofer'

task default: %w[test]

task :test do
   sh "script/cibuild"
   HTML::Proofer.new("./_site",
    {:url_ignore => [%r{[Cc]ardiff[Mm]athematics[Cc]ode[Cc]lub\.github\.io}]}).run
end

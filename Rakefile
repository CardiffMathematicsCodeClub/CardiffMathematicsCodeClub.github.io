require 'html/proofer'

task default: %w[test]

task :preview do
    sh "jekyll serve"
end

task :develop do
    sh "jekyll server --drafts"
end

task :test do
   sh "script/cibuild"
   HTML::Proofer.new("./_site",
    {:url_ignore => [%r{[Cc]ardiff[Mm]athematics[Cc]ode[Cc]lub\.github\.io}],
     :only_4xx => true}).run
end

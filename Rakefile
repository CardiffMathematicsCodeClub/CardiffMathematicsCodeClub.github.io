require 'fileutils'
require 'html/proofer'
require 'yaml'

task default: %w[help]
task :help do
  exec("rake -T")
end

desc 'List all the drafts currently on the site'
task :drafts do
  Dir.glob("_drafts/*.md") do |file|
    puts File.basename(file, ".md")
  end
end

desc 'Start working on a new post in _drafts'
task :newpost, [:name] do |t, args|

  # If _drafts doesn't exist, make it
  FileUtils.mkdir("_drafts") unless File.exists?("_drafts")

  # Make sure the file doesn't already exist
  if File.exists?("_drafts/#{args.name}.md")
    raise "_drafts/#{args.name} already exists"
  end

  # Copy the template over
  FileUtils.cp("templates/blogpost.md","_drafts/#{args.name}.md")

  puts "Draft post: _drafts/#{args.name}.md created"
end

desc 'Publish a post in drafts'
task :publishpost, [:name] do |t, args|

  # Check it exists
  if not File.exists?("_drafts/#{args.name}.md")
    raise "_drafts/#{args.name}.md doesn't exist"
  end

  # Next we need to get the current date
  time = Time.new
  date = time.strftime("%Y-%m-%d")

  # Move the blog post to be published and add the date to the filename
  FileUtils.mv("_drafts/#{args.name}.md", "_posts/#{date}-#{args.name}.md")

  puts "Published post _drafts/#{args.name}.md as _posts/#{date}-#{args.name}.md"

end

desc 'Create a new theme for the website'
task :newtheme, [:name, :author] do  |_, args|

  name = args.name.split.map(&:capitalize).join(' ')
  shortname = name.delete(' ').downcase

  # Make sure nobody else has made a theme by this name
  if File.exists?("css/#{shortname}.scss")
    raise "Sorry a theme called #{name} already exists"
  end

  puts "css/#{shortname}.css"

  # Otherwise create a new theme by that name
  FileUtils.cp("templates/theme.scss", "css/#{shortname}.scss")

  # Create a folder for them to used
  FileUtils.mkdir "_sass/_themes/_#{shortname}"

  # Copy over the example theme part file
  FileUtils.cp("templates/themepart.scss", "_sass/_themes/_#{shortname}/example.scss")

  # Finally install the theme on the website
  themes_f = File.open("_data/themes.yml", 'a')

  # Write the data we need
  themes_f.puts "\n- name: #{name}\n  shortname: #{shortname}\n  version: 0.1\n  author: #{args.author}\n"

  # Close the file
  themes_f.close

  # Give feedback
  puts "Theme template for #{name} created"

end

desc 'Build and preview the site as it would be seen on github'
task :preview do
    sh "bundle exec jekyll serve"
end

desc 'Run the jekyll server, including all the drafts in _drafts'
task :develop do
    sh "bundle exec jekyll serve --drafts"
end

desc 'Build the site and run the tests'
task :test do
   sh "script/cibuild"
   HTML::Proofer.new("./_site",
                     { :check_html => true,
                       :only_4xx => true,
                       :url_ignore => [%r{[Cc]ardiff[Mm]athematics[Cc]ode[Cc]lub\.github\.io}]}).run
end

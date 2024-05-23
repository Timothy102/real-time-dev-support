import SideBarLayout from '../../layout/SideBarLayout';
import SignInWithGitHub from '../../components/SignInWithGithub';

const CreatePage: React.FC = () => {

  return (
    <SideBarLayout>
      <div className='mb-10'>
        <h1 className="text-2xl font-bold text-gray-900 mb-4">Greptile - Real-Time Developer Support</h1>
        <h4 className="text-gray-900 mb-6 md:mb-8 lg:mb-10">
          Introducing Greptile, our cutting-edge automated technical support system designed for developers.
        </h4>
        <ol className="list-decimal ml-8">
          <li className="mb-4">
            <strong>Scope:</strong> Designed for developers who need immediate answers to bugs or code changes, our AI assistant provides contextual support to both internal teams and external customers.
          </li>
          <li className="mb-4">
            <strong>Product Workflow:</strong> 
            <ol className="list-decimal ml-8">
              <li className="mb-2">
                <strong>Easy Integration:</strong> Integrate Greptile into your dev support website, connect your GitHub, and select the appropriate repository. Embed custom iframes and HTML scripts to deploy the chatbots.
              </li>
              <li className="mb-10">
                <strong>Developer Interaction:</strong> Developers interact with the chatbot for support. If needed, the chatbot escalates the issue to the internal team via Slack, ensuring seamless human intervention.
              </li>
            </ol>
          </li>
        </ol>
        <SignInWithGitHub />
      </div>
    </SideBarLayout>
  );
};

export default CreatePage;